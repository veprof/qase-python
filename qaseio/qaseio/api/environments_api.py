# coding: utf-8

"""
    Qase.io API

    Qase API Specification.  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: support@qase.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from qaseio.api_client import ApiClient


class EnvironmentsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_environment(self, body, code, **kwargs):  # noqa: E501
        """Create a new environment.  # noqa: E501

        This method allows to create an environment in selected project.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_environment(body, code, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param EnvironmentCreate body: (required)
        :param str code: Code of project, where to search entities. (required)
        :return: IdResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_environment_with_http_info(body, code, **kwargs)  # noqa: E501
        else:
            (data) = self.create_environment_with_http_info(body, code, **kwargs)  # noqa: E501
            return data

    def create_environment_with_http_info(self, body, code, **kwargs):  # noqa: E501
        """Create a new environment.  # noqa: E501

        This method allows to create an environment in selected project.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_environment_with_http_info(body, code, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param EnvironmentCreate body: (required)
        :param str code: Code of project, where to search entities. (required)
        :return: IdResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'code']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_environment" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `create_environment`")  # noqa: E501
        # verify the required parameter 'code' is set
        if ('code' not in params or
                params['code'] is None):
            raise ValueError("Missing the required parameter `code` when calling `create_environment`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'code' in params:
            path_params['code'] = params['code']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['TokenAuth']  # noqa: E501

        return self.api_client.call_api(
            '/environment/{code}', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='IdResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_environment(self, code, id, **kwargs):  # noqa: E501
        """Delete environment.  # noqa: E501

        This method completely deletes an environment from repository.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_environment(code, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str code: Code of project, where to search entities. (required)
        :param int id: Identifier. (required)
        :return: IdResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_environment_with_http_info(code, id, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_environment_with_http_info(code, id, **kwargs)  # noqa: E501
            return data

    def delete_environment_with_http_info(self, code, id, **kwargs):  # noqa: E501
        """Delete environment.  # noqa: E501

        This method completely deletes an environment from repository.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_environment_with_http_info(code, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str code: Code of project, where to search entities. (required)
        :param int id: Identifier. (required)
        :return: IdResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['code', 'id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_environment" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'code' is set
        if ('code' not in params or
                params['code'] is None):
            raise ValueError("Missing the required parameter `code` when calling `delete_environment`")  # noqa: E501
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `delete_environment`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'code' in params:
            path_params['code'] = params['code']  # noqa: E501
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['TokenAuth']  # noqa: E501

        return self.api_client.call_api(
            '/environment/{code}/{id}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='IdResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_environment(self, code, id, **kwargs):  # noqa: E501
        """Get a specific environment.  # noqa: E501

        This method allows to retrieve a specific environment.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_environment(code, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str code: Code of project, where to search entities. (required)
        :param int id: Identifier. (required)
        :return: EnvironmentResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_environment_with_http_info(code, id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_environment_with_http_info(code, id, **kwargs)  # noqa: E501
            return data

    def get_environment_with_http_info(self, code, id, **kwargs):  # noqa: E501
        """Get a specific environment.  # noqa: E501

        This method allows to retrieve a specific environment.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_environment_with_http_info(code, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str code: Code of project, where to search entities. (required)
        :param int id: Identifier. (required)
        :return: EnvironmentResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['code', 'id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_environment" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'code' is set
        if ('code' not in params or
                params['code'] is None):
            raise ValueError("Missing the required parameter `code` when calling `get_environment`")  # noqa: E501
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_environment`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'code' in params:
            path_params['code'] = params['code']  # noqa: E501
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['TokenAuth']  # noqa: E501

        return self.api_client.call_api(
            '/environment/{code}/{id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='EnvironmentResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_environments(self, code, **kwargs):  # noqa: E501
        """Get all environments.  # noqa: E501

        This method allows to retrieve all environments stored in selected project.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_environments(code, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str code: Code of project, where to search entities. (required)
        :param int limit: A number of entities in result set.
        :param int offset: How many entities should be skipped.
        :return: EnvironmentListResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_environments_with_http_info(code, **kwargs)  # noqa: E501
        else:
            (data) = self.get_environments_with_http_info(code, **kwargs)  # noqa: E501
            return data

    def get_environments_with_http_info(self, code, **kwargs):  # noqa: E501
        """Get all environments.  # noqa: E501

        This method allows to retrieve all environments stored in selected project.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_environments_with_http_info(code, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str code: Code of project, where to search entities. (required)
        :param int limit: A number of entities in result set.
        :param int offset: How many entities should be skipped.
        :return: EnvironmentListResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['code', 'limit', 'offset']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_environments" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'code' is set
        if ('code' not in params or
                params['code'] is None):
            raise ValueError("Missing the required parameter `code` when calling `get_environments`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'code' in params:
            path_params['code'] = params['code']  # noqa: E501

        query_params = []
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'offset' in params:
            query_params.append(('offset', params['offset']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['TokenAuth']  # noqa: E501

        return self.api_client.call_api(
            '/environment/{code}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='EnvironmentListResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_environment(self, body, code, id, **kwargs):  # noqa: E501
        """Update environment.  # noqa: E501

        This method updates an environment.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_environment(body, code, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param EnvironmentUpdate body: (required)
        :param str code: Code of project, where to search entities. (required)
        :param int id: Identifier. (required)
        :return: IdResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_environment_with_http_info(body, code, id, **kwargs)  # noqa: E501
        else:
            (data) = self.update_environment_with_http_info(body, code, id, **kwargs)  # noqa: E501
            return data

    def update_environment_with_http_info(self, body, code, id, **kwargs):  # noqa: E501
        """Update environment.  # noqa: E501

        This method updates an environment.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_environment_with_http_info(body, code, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param EnvironmentUpdate body: (required)
        :param str code: Code of project, where to search entities. (required)
        :param int id: Identifier. (required)
        :return: IdResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'code', 'id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_environment" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `update_environment`")  # noqa: E501
        # verify the required parameter 'code' is set
        if ('code' not in params or
                params['code'] is None):
            raise ValueError("Missing the required parameter `code` when calling `update_environment`")  # noqa: E501
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `update_environment`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'code' in params:
            path_params['code'] = params['code']  # noqa: E501
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['TokenAuth']  # noqa: E501

        return self.api_client.call_api(
            '/environment/{code}/{id}', 'PATCH',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='IdResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)