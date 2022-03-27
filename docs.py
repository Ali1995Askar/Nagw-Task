
XLSX_FORMULA = '=HYPERLINK(CONCATENATE("{}", "{}"), "{}")'

FILE_NAME = 'books.xlsx'

RESPONSE = {
    'res': '{}',
    'statud_code': '{}'
}


GET_BOOKS_REQUEST_STRUCTURE= {
'General':{
            'Request URL': 'https://nagwa-task-excel-api.herokuapp.com/api/books',
            'Request Method': 'GET'
        },

'Request Header':{
            'Content-Type': 'application/json',
            'Accept': 'json'
        }
    }


CREATE_BOOK_REQUEST_STRUCTURE= {
'General':{
            'Request URL': 'https://nagwa-task-excel-api.herokuapp.com/api/books',
            'Request Method': 'POST'
        },

'Request Header':{
            'Content-Type': 'application/json',
            'Accept': 'json'
        },
'Request Body':{
            'order': 'order of book : str',
            'book': {
                        'name': 'name of book : str',
                        'url': 
                        """url of book should not contain This sub str [', CONTAIN, "]"""
                    },
            'author': {
                        'name': 'name of author : str',
                        'url': 
                        """url of author should not contain This sub str [', CONTAIN, "]"""
                    }, 
            'country': {
                        'name': 'name of country : str',
                        'url': 
                        """url of country should not contain This sub str [', CONTAIN, "]"""
                    }, 
        }
    }


UPDATE_BOOK_REQUEST_STRUCTURE= {
'General':{
            'Request URL': 'https://nagwa-task-excel-api.herokuapp.com/api/books',
            'Request Method': 'POST'
        },

'Request Header':{
            'Content-Type': 'application/json',
            'Accept': 'json'
        },
'Request Body':{
            'id': 'id of row to update data and data to be updated ',
            'order': 'new order of book :  str',
            'book': {
                        'name': 'new name of book : str',
                        'url': 
                        """new url of book should not contain This sub str [', CONTAIN, "]"""
                    },
            'author': {
                        'name': 'new name of author : str',
                        'url': 
                        """new url of author should not contain This sub str [', CONTAIN, "]"""
                    }, 
            'country': {
                        'name': 'new name of country : str',
                        'url': 
                        """new url of country should not contain This sub str [', CONTAIN, "]"""
                    }, 
        }
    }


DELETE_BOOK_REQUEST_STRUCTURE= {
'General':{
            'Request URL': 'https://nagwa-task-excel-api.herokuapp.com/api/books',
            'Request Method': 'DELETE'
        },

'Request Header':{
            'Content-Type': 'application/json',
            'Accept': 'json'
        },
'Request Body':{
            'id': 'id of row to delete : int'  
    }
}