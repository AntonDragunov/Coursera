class Layer:

    def __init__(self, name='Layer'):
        self.next_layer = None
        self.name = name

    def __call__(self, layer, *args, **kwargs):
        self.next_layer = layer
        return layer


class Input(Layer):

    def __init__(self, inputs):
        super().__init__('Input')
        self.inputs = inputs


class Dense(Layer):
    name = 'Dense'

    def __init__(self, inputs, outputs, activation):
        super().__init__('Dense')
        self.inputs = inputs
        self.outputs = outputs
        self.activation = activation


class NetworkIterator:
    def __init__(self, network):
        self.network = network

    def __iter__(self):
        layer = self.network
        while layer:
            yield layer
            layer = layer.next_layer



first_layer = Layer()
next_layer = first_layer(Layer())
next_layer = next_layer(Layer())

# class NetworkIterator:
#
#
#     for x in NetworkIterator(network):
#         print(x.name)