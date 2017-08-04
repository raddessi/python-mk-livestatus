from mk_livestatus import Query


def test_query_1():
    q = Query(None, 'hosts')
    q.columns('name', 'groups')
    q.stats('state = 0')
    q.filter('state = 0')
    expected = '''GET hosts
Columns: name groups
Stats: state = 0
Filter: state = 0
OutputFormat: json
ColumnHeaders: on
'''
    assert str(q) == expected


def test_query_2():
    q = Query(None, 'services')
    q.columns('host_name', 'service_description', 'plugin_output', 'state')
    q.stats('state = 0')
    q.filter('host_name = localhost')
    expected = '''GET services
Columns: host_name service_description plugin_output state
Stats: state = 0
Filter: host_name = localhost
OutputFormat: json
ColumnHeaders: on
'''
    assert str(q) == expected


def test_query_3():
    """Test Query.stats_and."""
    q = Query(None, 'services')
    q.columns('host_name', 'service_description', 'plugin_output', 'state')
    q.stats('last_hard_state = 2')
    q.stats('acknowledged = 0')
    q.stats_and('2')
    q.filter('host_name = localhost')
    expected = '''GET services
Columns: host_name service_description plugin_output state
Stats: last_hard_state = 2
Stats: acknowledged = 0
StatsAnd: 2
Filter: host_name = localhost
OutputFormat: json
ColumnHeaders: on
'''
    assert str(q) == expected


def test_query_4():
    """Test Query.stats_or."""
    q = Query(None, 'services')
    q.columns('host_name', 'service_description', 'plugin_output', 'state')
    q.stats('last_hard_state = 2')
    q.stats('acknowledged = 0')
    q.stats_or('2')
    q.filter('host_name = localhost')
    expected = '''GET services
Columns: host_name service_description plugin_output state
Stats: last_hard_state = 2
Stats: acknowledged = 0
StatsOr: 2
Filter: host_name = localhost
OutputFormat: json
ColumnHeaders: on
'''
    assert str(q) == expected


def test_query_5():
    """Test Query.stats_group_by."""
    q = Query(None, 'services')
    q.columns('host_name', 'service_description', 'plugin_output', 'state')
    q.stats('last_hard_state = 2')
    q.stats('acknowledged = 0')
    q.stats_group_by('service_description')
    q.filter('host_name = localhost')
    expected = '''GET services
Columns: host_name service_description plugin_output state
Stats: last_hard_state = 2
Stats: acknowledged = 0
StatsGroupBy: service_description
Filter: host_name = localhost
OutputFormat: json
ColumnHeaders: on
'''
    assert str(q) == expected
