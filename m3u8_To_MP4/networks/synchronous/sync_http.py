import urllib.error
import urllib.parse
import urllib.request
import urllib.response

from m3u8_To_MP4.networks import http_base


def http_get_header(customized_http_header):
    request_header = dict()

    user_agent = http_base.random_user_agent()
    request_header['User-Agent'] = user_agent

    if customized_http_header is not None:
        request_header.update(customized_http_header)

    return request_header


def retrieve_resource_from_url(url, max_retry_times=5, timeout=30,
							   customized_http_header=None):
    response_code = -1
    response_content = None

    for num_retry in range(max_retry_times):
        headers = http_get_header(customized_http_header)

        try:
            request = urllib.request.Request(url=url, headers=headers)

            with urllib.request.urlopen(url=request,
                                        timeout=timeout) as response:
                response_code = response.getcode()
                response_content = response.read()

            if response_code == 200:
                break
        except urllib.error.HTTPError as he:
            response_code = he.code
        except urllib.error.ContentTooShortError:
            response_code = -2  # -2:ctse
        except urllib.error.URLError:
            response_code = -3  # -3:URLError
        except Exception:
            response_code = -4  # other error
        finally:
            timeout += 2

    return response_code, response_content
