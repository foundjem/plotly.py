

import _plotly_utils.basevalidators


class TokenValidator(_plotly_utils.basevalidators.StringValidator):

    def __init__(
        self, plotly_name='token', parent_name='ohlc.stream', **kwargs
    ):
        super(TokenValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop('edit_type', 'calc'),
            no_blank=kwargs.pop('no_blank', True),
            role=kwargs.pop('role', 'info'),
            strict=kwargs.pop('strict', True),
            **kwargs
        )


import _plotly_utils.basevalidators


class MaxpointsValidator(_plotly_utils.basevalidators.NumberValidator):

    def __init__(
        self, plotly_name='maxpoints', parent_name='ohlc.stream', **kwargs
    ):
        super(MaxpointsValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop('edit_type', 'calc'),
            max=kwargs.pop('max', 10000),
            min=kwargs.pop('min', 0),
            role=kwargs.pop('role', 'info'),
            **kwargs
        )
