import ccircle
import connection

con = connection.create()
con.send('set_name', {'name': 'Unknown'})
args = {
    'vx':20,
    'vy':-0,
}
con.send('set_velocity', args)

# Write code to make money and kill the evil cat!
# See readme.txt !