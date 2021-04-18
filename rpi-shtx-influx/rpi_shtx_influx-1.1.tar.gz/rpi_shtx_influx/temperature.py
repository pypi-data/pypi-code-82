#!/usr/bin/env python3

import logging
import adafruit_si7021
from influxdb_client import InfluxDBClient
from influxdb_client.client.write_api import SYNCHRONOUS
import board

log = logging.getLogger(__name__)

class TemperatureReader:
        def __init__(self, bucket, org, token, url, 
                hostname, max_same_reads=60) -> None:
            self._bucket = bucket
            self._org = org
            self._token = token
            self._url = url
            self._hostname = hostname
            self._sensor = None
            self._influx = None
            self._influx_init_count = 0
            self._sensor_init_count = 0
            self._last_temperature = 0
            self._last_humidity = 0
            self._same_reading = 0
            self._max_same_reads = max_same_reads
        
        def ensure_sensor(self) -> None:
                if not self._sensor:
                        log.debug("Initializing temp sensor")
                        self._sensor_init_count += 1
                        self._sensor = adafruit_si7021.SI7021(board.I2C())
        def ensure_influx(self) -> None:
                if not self._influx:
                        log.debug("Initializing Influx client")
                        self._influx_init_count += 1
                        client = InfluxDBClient(url=self._url, token=self._token, org=self._org)
                        self._influx = client.write_api(write_options=SYNCHRONOUS)
        def temperature_metrics(self) -> list(str):
                self.ensure_sensor()
                temperature = self._sensor.temperature
                humidity = self._sensor.relative_humidity
                if self._last_temperature == temperature and self._last_humidity == humidity:
                        self._same_reading += 1
                else:
                        self._same_reading = 0
                if self._same_reading > self._max_same_reads:
                        log.error(f'Same reading from the sensors {self._same_reading} in a row. Resetting sensor.')
                        self._sensor = None
                return [
                        f'temperature,host={self._hostname} degrees_c={temperature}',
                        f'humidity,host={self._hostname} humidity_pct={humidity}',
                ]
        def internal_metrics(self) -> list(str):
                return [                
                        f'sensor_initialized,host={self._hostname} count={self._sensor_init_count}',
                        f'influx_initialized,host={self._hostname}, count={self._influx_init_count}',
                ]
        def write_metrics(self, metrics: list(str)) -> None:
                log.debug(f"Going to write to influx: {metrics}")
                try:
                        self._influx.write(bucket=self._bucket, record=metrics)
                except:
                        log.error("Failed to write to Influx. Will try to reconnect next time.")
                        self._influx = None
        def fetch_and_write_metrics(self) -> None:
                self.write_metrics(self.temperature_metrics() + self.internal_metrics())
