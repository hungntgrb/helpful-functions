def c50(text: str):
    return text.center(50, '-')


def _print_initial_data(serializer):
    print(c50(' serializer.initial_data '),
          serializer.initial_data, sep='\n')


def _print_serializer_validate(data):
    print(c50(' serializer.validate(data) '),
          f'  Type: {type(data)}',
          f'  Data: {data}',
          sep='\n')


def _print_serializer_create(validated_data):
    print(c50(' serializer.create(validated_data) '),
          f'  Type: {type(validated_data)}',
          f'  Validated_data: {validated_data}',
          sep='\n')


def _print_serializer_update(serializer, validated_data):
    print(c50(' serializer.instance '),
          f'  Type: {type(serializer.instance)}',
          f'  Instance: {serializer.instance}',
          sep='\n')
    print(c50(' serializer.update( validated_data ) '),
          f'  Type: {type(validated_data)}',
          f'  validated_data: {validated_data}',
          sep='\n')


def _print_request_data(request):
    print(c50(' request.data '),
          request.data, sep='\n')


def _print_serializer_to_internal_value(data):
    print(c50(' serializer.to_internal_value(data) '),
          f'  data: {data}',
          f'  type: {type(data)}',
          sep='\n')


def _print_serializer_to_representation(instance):
    print(c50(' serializer.to_representation(instance) '),
          f'  instance: {instance}',
          f'  type: {type(instance)}',
          sep='\n')


def _print_serializer_validate_field(data):
    print(c50(' serializer.validate_<field>(data) '),
          f'  data: {data}',
          f'  type: {type(data)}',
          sep='\n')


def _print_serializer_validate(attrs):
    print(c50(' serializer.validate(attrs) '),
          f'  data: {attrs}',
          f'  type: {type(attrs)}',
          sep='\n')
