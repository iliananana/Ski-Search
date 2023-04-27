from flask import Flask, render_template, request, session
import snowfall
import a_star
import mm_to_coord
app=Flask(__name__)
app.secret_key = "its good!"

markers=[
    {
    'lat':40.573808,
    'lon':-105.0826341,
    'popup':'Starting at the CSU CS Building'
    }
]
resorts = snowfall.march_resorts_list

@app.route('/', methods=['GET'])
def root():

    if request.method == "GET":
        goal = request.args.get("resort", default=None, type=str)
        yesbtn = request.args.get("yesbtn", default=None, type=str)
        nobtn = request.args.get("nobtn", default=None, type=str)

        if not goal:
            print("the user has not selected a resort yet")
        elif yesbtn:
            status, val1, val2, val3, val4 = a_star.a_star_search('Colorado State University', session.get("suggested_goal"), session.get("frontier"), session.get("visited"), session.get("total_cost"))
            if status == "reroute":
                session["suggested_goal"] = val1
                session["frontier"] = val2
                session["visited"] = val3
                session["total_cost"] = val4
                return render_template('index.html',markers=markers,resorts=resorts,reroute=val1)
            else:
                path = val1
                total_cost = val2
                new_goal = val3

                session["total_cost"] = total_cost
                session["new_goal"] = new_goal

                print('initial goal:', session.get("goal"))
                print('updated goal:', new_goal)
                print('The optimal path to take is:', path)
                print('The total cost is:', total_cost[new_goal])
                print("final goal is: " + new_goal)
                goal_row = mm_to_coord.resort_coords.loc[mm_to_coord.resort_coords['resorts'] == new_goal]
                markers.append({
                    'lat': goal_row['coordinates'].iloc[0][0],
                    'lon': goal_row['coordinates'].iloc[0][1],
                    'popup': 'The optimal place to ski is ' + new_goal + '!'
                })
                return render_template('index.html',markers=markers,resorts=resorts,reroute=None)
            
        elif nobtn:
            status, val1, val2, val3, val4 = a_star.a_star_search('Colorado State University', session.get("goal"), session.get("frontier"), session.get("visited"), session.get("total_cost"))
            if status == "reroute":
                session["suggested_goal"] = val1
                session["frontier"] = val2
                session["visited"] = val3
                session["total_cost"] = val4
                return render_template('index.html',markers=markers,resorts=resorts,reroute=val1)
            else:
                path = val1
                total_cost = val2
                new_goal = val3

                session["total_cost"] = total_cost
                session["new_goal"] = new_goal

                print('initial goal:', session.get("goal"))
                print('updated goal:', new_goal)
                print('The optimal path to take is:', path)
                print('The total cost is:', total_cost[new_goal])
                print("final goal is: " + new_goal)
                goal_row = mm_to_coord.resort_coords.loc[mm_to_coord.resort_coords['resorts'] == new_goal]
                markers.append({
                    'lat': goal_row['coordinates'].iloc[0][0],
                    'lon': goal_row['coordinates'].iloc[0][1],
                    'popup': 'The optimal place to ski is ' + new_goal + '!'
                })
                return render_template('index.html',markers=markers,resorts=resorts,reroute=None)
            
        else:
            print(f"the user has selected {goal}")
            session["goal"] = goal

            status, val1, val2, val3, val4 = a_star.a_star_search('Colorado State University', goal, None, None, None)
            if status == "reroute":
                session["suggested_goal"] = val1
                session["frontier"] = val2
                session["visited"] = val3
                session["total_cost"] = val4
                return render_template('index.html',markers=markers,resorts=resorts,reroute=val1)
            else:
                path = val1
                total_cost = val2
                new_goal = val3

                session["total_cost"] = total_cost
                session["new_goal"] = new_goal

                print('initial goal:', session.get("goal"))
                print('updated goal:', new_goal)
                print('The optimal path to take is:', path)
                print('The total cost is:', total_cost[new_goal])
                print("final goal is: " + new_goal)
                # works for no crashes
                goal_row = mm_to_coord.resort_coords.loc[mm_to_coord.resort_coords['resorts'] == new_goal]
                markers.append({
                    'lat': goal_row['coordinates'].iloc[0][0],
                    'lon': goal_row['coordinates'].iloc[0][1],
                    'popup': 'The optimal place to ski is ' + new_goal + '!'
                })
                return render_template('index.html',markers=markers,resorts=resorts,reroute=None)
            
    return render_template('index.html',markers=markers,resorts=resorts,reroute=None)

if __name__ == '__main__':
    app.run(host="localhost", port=8080, debug=True)
