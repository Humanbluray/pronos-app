import sqlite3


def max_liste():
    conn = sqlite3.connect("pornos.db")
    cur = conn.cursor()
    cur.execute("SELECT id FROM lists ORDER by id DESC")
    res = cur.fetchone()
    conn.commit()
    conn.close()
    return res[0]


def id_by_player_name(player_name):
    conn = sqlite3.connect("pornos.db")
    cur = conn.cursor()
    cur.execute("SELECT id FROM players WHERE player_name = ?", (player_name,))
    res = cur.fetchone()
    conn.commit()
    conn.close()
    return res[0]


print(id_by_player_name("carlos"))


def nb_listes_by_player_id(player_id):
    conn = sqlite3.connect("pornos.db")
    cur = conn.cursor()
    cur.execute("SELECT count(id) FROM details WHERE player_id = ?", (player_id,))
    res = cur.fetchone()
    conn.commit()
    conn.close()
    return res[0]


def moyenne_points_liste_by_player_id(player_id):
    conn = sqlite3.connect("pornos.db")
    cur = conn.cursor()
    cur.execute("SELECT avg(points) FROM details WHERE player_id = ?", (player_id, ))
    res = cur.fetchone()
    conn.commit()
    conn.close()
    return res[0]


def goal_average_by_player_id(player_id):
    conn = sqlite3.connect("pornos.db")
    cur = conn.cursor()
    cur.execute("SELECT sum(points) FROM details WHERE player_id = ?", (player_id, ))
    res = cur.fetchone()
    conn.commit()
    conn.close()
    return res[0]


def nom_listes():
    conn = sqlite3.connect("pornos.db")
    cur = conn.cursor()
    cur.execute("SELECT list_name FROM lists ORDER by id")
    res = cur.fetchall()
    final = []
    for row in res:
        final.append(row[0])
    conn.commit()
    conn.close()
    return final


def id_liste_by_name(list_name):
    conn = sqlite3.connect("pornos.db")
    cur = conn.cursor()
    cur.execute("SELECT id FROM lists WHERE list_name = ?", (list_name,))
    res = cur.fetchone()
    conn.commit()
    conn.close()
    return res[0]


# print(id_liste_by_name("list 45"))


def listes_players():
    conn = sqlite3.connect("pornos.db")
    cur = conn.cursor()
    cur.execute("""SELECT player_name FROM players""")
    res = cur.fetchall()
    final= []
    for row in res:
        final.append(row[0])
    conn.commit()
    conn.close()
    return final


def compte_points(rang):
    if rang == 1:
        return 10
    elif rang == 2:
        return 7
    elif rang == 3:
        return 5
    elif rang == 4:
        return 3
    elif rang == 5:
        return 2
    elif rang == 6:
        return 1
    else:
        return 0


def goal_average():
    conn = sqlite3.connect("pornos.db")
    cur = conn.cursor()
    cur.execute("""SELECT player_id,
                    (SELECT player_name FROM players WHERE players.id = details.player_id) as player,
                    sum(points) as global FROM details
                    GROUP BY player_id ORDER BY global DESC """)
    result = cur.fetchall()
    conn.commit()
    conn.close()
    return result


def classement_par_liste():
    conn = sqlite3.connect("pornos.db")
    cur = conn.cursor()
    cur.execute(""" SELECT list_id,
                    (SELECT player_name FROM players WHERE players.id = details.player_id) as player,
                    (select list_name FROM lists WHERE lists.id = details.list_id) as list_name,
                    points FROM details ORDER BY points DESC""")
    res = cur.fetchall()
    final = []

    for data in res:
        i= 0
        rang = 1
        while i < len(res):
            if res[i][2] == data[2]:
                if res[i][3] > data[3]:
                    rang += 1
            i += 1

        points_gen = compte_points(rang)
        data = data + (rang, points_gen)
        final.append(data)

    r_final = []
    for data in final:
        dico = {"N° liste": data[0], "player": data[1], "liste": data[2], "points": data[3], 'rang': data[4],
                'points gen': data[5]}
        r_final.append(dico)

    conn.commit()
    conn.close()
    return r_final


def claseement_general(num_liste):
    players = listes_players()
    datas = classement_par_liste()

    # classment j-1
    classement_avant = []
    for player in players:
        total = 0
        ga = 0
        nb_listes = 0
        for data in datas:
            if data['N° liste'] <= num_liste - 1:
                if data['player'] == player:
                    nb_listes += 1
                    total += data["points gen"]
                    ga += data['points']
        dico = {"player": player, "points": total, "GA": ga, "nb listes": nb_listes}
        classement_avant.append(dico)

        # trouver le rang
        for data in classement_avant:
            rang = 1
            i = 0
            while i < len(classement_avant):
                if classement_avant[i]['points'] > data['points']:
                    rang += 1
                i += 1
            data['rang'] = rang

    # classement
    classement = []
    for player in players:
        total = 0
        ga = 0
        nb_listes = 0
        for data in datas:
            if data['N° liste'] <= num_liste:
                if data['player'] == player:
                    nb_listes += 1
                    total += data["points gen"]
                    ga += data['points']
        dico = {"player": player, "points": total, "GA": ga, "nb listes": nb_listes}
        classement.append(dico)

    # trouver le rang
    for data in classement:
        rang = 1
        i = 0
        while i < len(classement):
            if classement[i]['points'] > data['points']:
                rang += 1
            i += 1
        data['rang'] = rang

    # comparer les rangs avant et actuels
    for data in classement:
        for row in classement_avant:
            if row['player'] == data['player']:
                data['rang j-1'] = row["rang"]

    for data in classement:
        if data["rang"] < data["rang j-1"]:
            data["evolution"] = "up"
        elif data['rang'] > data['rang j-1']:
            data["evolution"] = "down"
        else:
            data["evolution"] = "-"

    # ranger par ordre croissant de rang
    liste_classee = []
    for i in range(16):
        for data in classement:
            if data['rang'] == i:
                liste_classee.append(data)

    return liste_classee


# rech_list = "list 4"
# rech_num = 14
# datas = list(filter(lambda x: rech_num == x['N° liste'], classement_par_liste()))
#
# for data in datas:
#     print(data)
