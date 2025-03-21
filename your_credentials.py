import re

_credentials = {
    # Mongo Paths + URI
    "MONGODB_URI": "mongodb+srv://nicolas:<PWD>@escapegame.pypkq.mongodb.net/?retryWrites=true&w=majority&appName=EscapeGame",
    "SHARED_LIB_PATH": "/Users/nicolas.benhamou/qe-python/mongo_crypt_shared_v1-macos-arm64-enterprise-8.0.1/lib/mongo_crypt_v1.dylib",
}


def check_for_placeholders():
    """check if credentials object contains placeholder values"""
    error_buffer = []
    placeholder_pattern = re.compile("^<.*>$")
    for key, value in _credentials.items():
        # check for placeholder text
        if placeholder_pattern.match(str(value)):
            error_message = (
                f"You must fill out the {key} field of your credentials object."
            )
            error_buffer.append(error_message)
        # check if value is empty
        elif not value:
            error_message = (
                f"The value for {key} is empty. Please enter something for this value."
            )
    # raise an error if errors in buffer
    if error_buffer:
        message = "\n".join(error_buffer)
        raise ValueError(message)


def get_credentials():
    """return credentials object and ensure it has been populated"""
    check_for_placeholders()
    return _credentials