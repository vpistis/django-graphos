from django.template.loader import render_to_string

from .base import BaseChart


class LineChart( BaseChart ):
    def get_template( self ):
        return "graphos/gchart/line_chart.html"


class ColumnChart( BaseChart ):
    def get_template( self ):
        return "graphos/gchart/column_chart.html"


class BarChart( BaseChart ):
    def get_template( self ):
        return "graphos/gchart/bar_chart.html"

    def get_options( self ):
        options = super( BarChart, self ).get_options()
        if not 'vAxis' in options:
            vaxis = self.data_source.get_header()[0]
            options['vAxis'] = {'title': vaxis}
        return options


class CandlestickChart( BaseChart ):
    def get_template( self ):
        return "graphos/gchart/candlestick_chart.html"


class PieChart( BaseChart ):
    def get_template( self ):
        return "graphos/gchart/pie_chart.html"


class PieChartEuros( BaseChart ):
    '''
    Return a pie chart with euros symbol prefix to value
    '''
    def get_template( self ):
        return "graphos/gchart/pie_chart_euros.html"


class TreeMapChart( BaseChart ):
    def get_template( self ):
        return "graphos/gchart/treemap_chart.html"
