# Copyright (c) Microsoft Corporation.
# Licensed under the MIT license.

class BaseConfig(object):

    # Can be set to 'MasterUser' or 'ServicePrincipal'
    AUTHENTICATION_MODE = 'ServicePrincipal'

    # Workspace Id in which the report is present
    WORKSPACE_ID = '0957e05f-fea1-49ed-8944-451bba07099e'
    
    # Report Id for which Embed token needs to be generated
    REPORT_ID = '157406c9-d16e-41f3-9c25-33614164fadb'
    
    # Id of the Azure tenant in which AAD app and Power BI report is hosted. Required only for ServicePrincipal authentication mode.
    TENANT_ID = '807ebfbb-86ca-41a5-87df-d9c348b89f83'
    
    # Client Id (Application Id) of the AAD app
    CLIENT_ID = 'bbc50297-763f-4087-b95b-42b2eee8694b'
    
    # Client Secret (App Secret) of the AAD app. Required only for ServicePrincipal authentication mode.
    CLIENT_SECRET = '9nC7Q~C3EuXU6msq8HIbpMQ6C3jICS8x6wDlF'
    
    # Scope of AAD app. Use the below configuration to use all the permissions provided in the AAD app through Azure portal.
    SCOPE = ['https://analysis.windows.net/powerbi/api/.default']
    
    # URL used for initiating authorization request
    AUTHORITY = 'https://login.microsoftonline.com/organizations'
    
    # Master user email address. Required only for MasterUser authentication mode.
    POWER_BI_USER = ''
    
    # Master user email password. Required only for MasterUser authentication mode.
    POWER_BI_PASS = ''