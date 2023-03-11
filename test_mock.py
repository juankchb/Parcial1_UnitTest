from unittest.mock import patch, Mock
from descargar_archivo import descargar_html


@patch('boto3.client')
@patch('requests.get')
def test_descargar_html_mock(mock_get, mock_client):
    mock_response = Mock()
    mock_response.text = '<html><body>Test HTML</body></html>'
    mock_response.content = b'Test HTML'
    mock_get.return_value = mock_response
    mock_client.return_value = Mock()
    descargar_html()