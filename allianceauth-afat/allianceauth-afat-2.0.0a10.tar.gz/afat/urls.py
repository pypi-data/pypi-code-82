"""
url configuration
"""

from django.conf.urls import url

from afat.views import dashboard, fatlinks, statistics

app_name: str = "afat"

urlpatterns = [
    # dashboard
    url(r"^$", dashboard.overview, name="dashboard"),
    # stats main page
    url(r"^statistics/$", statistics.overview, name="statistics_overview"),
    url(
        r"^statistics/(?P<year>[0-9]+)/$",
        statistics.overview,
        name="statistics_overview",
    ),
    # stats corp
    url(
        r"^statistics/corporation/$",
        statistics.corporation,
        name="statistics_corporation",
    ),
    url(
        r"^statistics/corporation/(?P<corpid>[0-9]+)/$",
        statistics.corporation,
        name="statistics_corporation",
    ),
    url(
        r"^statistics/corporation/(?P<corpid>[0-9]+)/(?P<year>[0-9]+)/$",
        statistics.corporation,
        name="statistics_corporation",
    ),
    url(
        r"^statistics/corporation/(?P<corpid>[0-9]+)/(?P<year>[0-9]+)/(?P<month>[0-9]+)/$",
        statistics.corporation,
        name="statistics_corporation",
    ),
    # stats char
    url(r"^statistics/character/$", statistics.character, name="statistics_character"),
    url(
        r"^statistics/character/(?P<charid>[0-9]+)/$",
        statistics.character,
        name="statistics_character",
    ),
    url(
        r"^statistics/character/(?P<charid>[0-9]+)/(?P<year>[0-9]+)/(?P<month>[0-9]+)/$",
        statistics.character,
        name="statistics_character",
    ),
    # stats alliance
    url(r"^statistics/alliance/$", statistics.alliance, name="statistics_alliance"),
    url(
        r"^statistics/alliance/(?P<allianceid>[0-9]+)/$",
        statistics.alliance,
        name="statistics_alliance",
    ),
    url(
        r"^statistics/alliance/(?P<allianceid>[0-9]+)/(?P<year>[0-9]+)/$",
        statistics.alliance,
        name="statistics_alliance",
    ),
    url(
        r"^statistics/alliance/(?P<allianceid>[0-9]+)/(?P<year>[0-9]+)/(?P<month>[0-9]+)/$",
        statistics.alliance,
        name="statistics_alliance",
    ),
    # fatlinks list actions
    url(r"^fatlinks/$", fatlinks.overview, name="links"),
    url(r"^fatlinks/(?P<year>[0-9]+)/$", fatlinks.overview, name="links"),
    url(
        r"^fatlinks/link/create/esi-fatlink/$",
        fatlinks.create_esi_fatlink,
        name="fatlinks_create_esi_fatlink",
    ),
    # fatlink actions
    url(r"^fatlink/add/$", fatlinks.add_fatlink, name="fatlinks_add_fatlink"),
    url(
        r"^fatlink/create/esi-fatlink/callback/(?P<fatlink_hash>[a-zA-Z0-9]+)/$",
        fatlinks.create_esi_fatlink_callback,
        name="fatlinks_create_esi_fatlink_callback",
    ),
    url(
        r"^fatlink/create/clickable-fatlink/$",
        fatlinks.create_clickable_fatlink,
        name="fatlinks_create_clickable_fatlink",
    ),
    url(
        r"^fatlink/(?P<fatlink_hash>[a-zA-Z0-9]+)/details/$",
        fatlinks.details_fatlink,
        name="fatlinks_details_fatlink",
    ),
    url(
        r"^fatlink/(?P<fatlink_hash>[a-zA-Z0-9]+)/delete/$",
        fatlinks.delete_fatlink,
        name="fatlinks_delete_fatlink",
    ),
    url(
        r"^fatlink/(?P<fatlink_hash>[a-zA-Z0-9]+)/stop-esi-tracking/$",
        fatlinks.close_esi_fatlink,
        name="fatlinks_close_esi_fatlink",
    ),
    url(
        r"^fatlink/(?P<fatlink_hash>[a-zA-Z0-9]+)/re-open/$",
        fatlinks.reopen_fatlink,
        name="fatlinks_reopen_fatlink",
    ),
    # fat actions
    url(
        r"^fatlink/(?P<fatlink_hash>[a-zA-Z0-9]+)/register/$",
        fatlinks.add_fat,
        name="fatlinks_add_fat",
    ),
    url(
        r"^fatlink/(?P<fatlink_hash>[a-zA-Z0-9]+)/fat/(?P<fat>[0-9]+)/delete/$",
        fatlinks.delete_fat,
        name="fatlinks_delete_fat",
    ),
    # ajax calls :: dashboard
    url(
        r"^ajax/dashboard/fatlinks/recent/$",
        dashboard.ajax_get_recent_fatlinks,
        name="dashboard_ajax_get_recent_fatlinks",
    ),
    url(
        r"^ajax/dashboard/fats/recent/character/(?P<charid>[0-9]+)/$",
        dashboard.ajax_recent_get_fats_by_character,
        name="dashboard_ajax_get_recent_fats_by_character",
    ),
    # ajax calls :: fatlinks
    url(
        r"^ajax/fatlinks/fatlinks/year/(?P<year>[0-9]+)/$",
        fatlinks.ajax_get_fatlinks_by_year,
        name="fatlinks_ajax_get_fatlinks_by_year",
    ),
    url(
        r"^ajax/fatlinks/fatlink/(?P<fatlink_hash>[a-zA-Z0-9]+)/fats/$",
        fatlinks.ajax_get_fats_by_fatlink,
        name="fatlinks_ajax_get_fats_by_fatlink",
    ),
]
