import pysal as ps


def create_polymap(shp_path, pysal_shp_obj, geoid_column):
    assert shp_path is not ''

    split = shp_path.split('.')
    split[-1] = 'dbf'
    dbf_dir = '.'.join(split)
    dbf = ps.open(dbf_dir)

    assert geoid_column in dbf.header

    geoid_list = dbf.by_col_array(geoid_column)
    geom_list = [x for x in pysal_shp_obj]

    assert len(geoid_list) == len(geom_list)
    return {geoid_list[i][0]: geom_list[i] for i in range(len(geom_list))}
