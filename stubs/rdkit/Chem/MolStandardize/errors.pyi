class MolVSError(Exception): ...
class StandardizeError(MolVSError): ...
class ValidateError(MolVSError): ...
class StopValidateError(ValidateError): ...
