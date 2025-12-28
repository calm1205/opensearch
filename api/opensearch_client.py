from opensearchpy import OpenSearch

client = OpenSearch(
    hosts=[{"host": "opensearch", "port": 9200}],
    http_auth=None,
    use_ssl=False,
)
