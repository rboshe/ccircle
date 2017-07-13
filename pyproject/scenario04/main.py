import ccircle
import connection

con = connection.create()
con.send('set_name', {'name': 'Unknown'})
con.send('get_money')
con.send('send_money(California, -10000000000000')
con.send('get_player_id_by_name(California')

args = {
    'vx': 0,
    'vy': 0
}
con.send('set_velocity', args)
while True:
    con.send('get_player_ids')

# Write code to make money and kill the evil cat!
# See readme.txt !
