from typing import List

FindOneChannelQuery: List[str] = ["""
  query findOneChannel ($findOneChannelDto: FindOneChannelDto!) {
    findOneChannel (findOneChannelDto: $findOneChannelDto) {
      fqcn
      description
      publicKey
      publisherRole
      subscriberRole
      maxTimeout
      defaultTimeout
    }
  }
  """
]