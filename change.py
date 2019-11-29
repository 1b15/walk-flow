import pandas as pd
import matplotlib.pyplot as plt

if __name__ == '__main__':
    data = pd.read_csv("Basel_Daten.csv", delimiter=';')
    #Alle Orte
    locs = sorted(list(set(data['SiteName'])))
    #Were sortiert mach Orten
    data_list = {loc: data[data['SiteName'] == loc] for loc in locs}
    #Zusammenfassen in Stunden
    data_loc_list = {}
    for loc, loc_data in data_list.items():
        stamps = [x.split('+')[0] for x in loc_data['DateTimeFrom'].values]
        loc_data = loc_data.assign(Time=pd.to_datetime(stamps.copy(), format="%Y-%m-%dT%H:%M:%S"))
        loc_data = loc_data.set_index('Time')
        counts = loc_data.groupby('Time').resample('H')[['Total']].sum()
        counts['Stamp'] = counts.index.get_level_values(0)
        counts = counts.reset_index(drop=True)
        counts = counts.set_index('Stamp')
        counts['Year'] = counts.index.year
        counts['Month'] = counts.index.month
        counts['Weekday'] = counts.index.weekday
        counts['Hour'] = counts.index.hour
        print("[%s] done"%loc)
        data_loc_list[loc] = counts

    print(locs)

    data_by_day = {"%d:%d:%d"%(yk,mk,dk):dv.sort_values(by=['Hour']) for yk, yv in data_loc_list[locs[0]].groupby('Year')
                                                                         for mk, mv in yv.groupby('Month')
                                                                         for dk, dv in mv.groupby('Weekday')}
    for i in range(1, 10):
        print(list(data_by_day.values())[i])
        list(data_by_day.values())[i]['Total'].plot()
        plt.show()


