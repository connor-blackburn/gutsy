{"filter":false,"title":"app.py","tooltip":"/app.py","undoManager":{"mark":100,"position":100,"stack":[[{"start":{"row":14,"column":4},"end":{"row":14,"column":9},"action":"remove","lines":["hello"],"id":673},{"start":{"row":14,"column":4},"end":{"row":14,"column":5},"action":"insert","lines":["g"]}],[{"start":{"row":14,"column":4},"end":{"row":14,"column":5},"action":"remove","lines":["g"],"id":674},{"start":{"row":14,"column":4},"end":{"row":14,"column":15},"action":"insert","lines":["get_recipes"]}],[{"start":{"row":43,"column":42},"end":{"row":44,"column":0},"action":"insert","lines":["",""],"id":678},{"start":{"row":44,"column":0},"end":{"row":44,"column":4},"action":"insert","lines":["    "]},{"start":{"row":44,"column":4},"end":{"row":45,"column":0},"action":"insert","lines":["",""]},{"start":{"row":45,"column":0},"end":{"row":45,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":45,"column":4},"end":{"row":50,"column":46},"action":"insert","lines":["@app.route('/update_category/<category_id>', methods=['POST'])","def update_category(category_id):","    mongo.db.categories.update(","        {'_id': ObjectId(category_id)},","        {'category_name': request.form.get('category_name')})","    return redirect(url_for('get_categories'))"],"id":679}],[{"start":{"row":45,"column":0},"end":{"row":45,"column":4},"action":"remove","lines":["    "],"id":680}],[{"start":{"row":45,"column":20},"end":{"row":45,"column":28},"action":"remove","lines":["category"],"id":681}],[{"start":{"row":45,"column":20},"end":{"row":45,"column":27},"action":"insert","lines":["cuisine"],"id":682}],[{"start":{"row":45,"column":36},"end":{"row":45,"column":37},"action":"remove","lines":["y"],"id":683},{"start":{"row":45,"column":35},"end":{"row":45,"column":36},"action":"remove","lines":["r"]},{"start":{"row":45,"column":34},"end":{"row":45,"column":35},"action":"remove","lines":["o"]},{"start":{"row":45,"column":33},"end":{"row":45,"column":34},"action":"remove","lines":["g"]},{"start":{"row":45,"column":32},"end":{"row":45,"column":33},"action":"remove","lines":["e"]},{"start":{"row":45,"column":31},"end":{"row":45,"column":32},"action":"remove","lines":["t"]},{"start":{"row":45,"column":30},"end":{"row":45,"column":31},"action":"remove","lines":["a"]},{"start":{"row":45,"column":29},"end":{"row":45,"column":30},"action":"remove","lines":["c"]}],[{"start":{"row":45,"column":29},"end":{"row":45,"column":36},"action":"insert","lines":["cuisine"],"id":684}],[{"start":{"row":46,"column":18},"end":{"row":46,"column":19},"action":"remove","lines":["y"],"id":685},{"start":{"row":46,"column":17},"end":{"row":46,"column":18},"action":"remove","lines":["r"]},{"start":{"row":46,"column":16},"end":{"row":46,"column":17},"action":"remove","lines":["o"]},{"start":{"row":46,"column":15},"end":{"row":46,"column":16},"action":"remove","lines":["g"]},{"start":{"row":46,"column":14},"end":{"row":46,"column":15},"action":"remove","lines":["e"]},{"start":{"row":46,"column":13},"end":{"row":46,"column":14},"action":"remove","lines":["t"]},{"start":{"row":46,"column":12},"end":{"row":46,"column":13},"action":"remove","lines":["a"]},{"start":{"row":46,"column":11},"end":{"row":46,"column":12},"action":"remove","lines":["c"]}],[{"start":{"row":46,"column":11},"end":{"row":46,"column":12},"action":"insert","lines":["v"],"id":686}],[{"start":{"row":46,"column":11},"end":{"row":46,"column":12},"action":"remove","lines":["v"],"id":689}],[{"start":{"row":46,"column":11},"end":{"row":46,"column":18},"action":"insert","lines":["cuisine"],"id":690}],[{"start":{"row":46,"column":26},"end":{"row":46,"column":27},"action":"remove","lines":["y"],"id":691},{"start":{"row":46,"column":25},"end":{"row":46,"column":26},"action":"remove","lines":["r"]},{"start":{"row":46,"column":24},"end":{"row":46,"column":25},"action":"remove","lines":["o"]},{"start":{"row":46,"column":23},"end":{"row":46,"column":24},"action":"remove","lines":["g"]},{"start":{"row":46,"column":22},"end":{"row":46,"column":23},"action":"remove","lines":["e"]},{"start":{"row":46,"column":21},"end":{"row":46,"column":22},"action":"remove","lines":["t"]},{"start":{"row":46,"column":20},"end":{"row":46,"column":21},"action":"remove","lines":["a"]},{"start":{"row":46,"column":19},"end":{"row":46,"column":20},"action":"remove","lines":["c"]}],[{"start":{"row":46,"column":19},"end":{"row":46,"column":26},"action":"insert","lines":["cuisine"],"id":692}],[{"start":{"row":47,"column":22},"end":{"row":47,"column":23},"action":"remove","lines":["s"],"id":693},{"start":{"row":47,"column":21},"end":{"row":47,"column":22},"action":"remove","lines":["e"]},{"start":{"row":47,"column":20},"end":{"row":47,"column":21},"action":"remove","lines":["i"]},{"start":{"row":47,"column":19},"end":{"row":47,"column":20},"action":"remove","lines":["r"]},{"start":{"row":47,"column":18},"end":{"row":47,"column":19},"action":"remove","lines":["o"]},{"start":{"row":47,"column":17},"end":{"row":47,"column":18},"action":"remove","lines":["g"]},{"start":{"row":47,"column":16},"end":{"row":47,"column":17},"action":"remove","lines":["e"]},{"start":{"row":47,"column":15},"end":{"row":47,"column":16},"action":"remove","lines":["t"]},{"start":{"row":47,"column":14},"end":{"row":47,"column":15},"action":"remove","lines":["a"]},{"start":{"row":47,"column":13},"end":{"row":47,"column":14},"action":"remove","lines":["c"]}],[{"start":{"row":47,"column":13},"end":{"row":47,"column":20},"action":"insert","lines":["cuisine"],"id":694}],[{"start":{"row":47,"column":20},"end":{"row":47,"column":21},"action":"insert","lines":["s"],"id":695}],[{"start":{"row":47,"column":20},"end":{"row":47,"column":21},"action":"remove","lines":["s"],"id":696}],[{"start":{"row":48,"column":32},"end":{"row":48,"column":33},"action":"remove","lines":["y"],"id":697},{"start":{"row":48,"column":31},"end":{"row":48,"column":32},"action":"remove","lines":["r"]},{"start":{"row":48,"column":30},"end":{"row":48,"column":31},"action":"remove","lines":["o"]},{"start":{"row":48,"column":29},"end":{"row":48,"column":30},"action":"remove","lines":["g"]},{"start":{"row":48,"column":28},"end":{"row":48,"column":29},"action":"remove","lines":["e"]},{"start":{"row":48,"column":27},"end":{"row":48,"column":28},"action":"remove","lines":["t"]},{"start":{"row":48,"column":26},"end":{"row":48,"column":27},"action":"remove","lines":["a"]},{"start":{"row":48,"column":25},"end":{"row":48,"column":26},"action":"remove","lines":["c"]}],[{"start":{"row":48,"column":25},"end":{"row":48,"column":32},"action":"insert","lines":["cuisine"],"id":698}],[{"start":{"row":49,"column":17},"end":{"row":49,"column":18},"action":"remove","lines":["y"],"id":699},{"start":{"row":49,"column":16},"end":{"row":49,"column":17},"action":"remove","lines":["r"]},{"start":{"row":49,"column":15},"end":{"row":49,"column":16},"action":"remove","lines":["o"]},{"start":{"row":49,"column":14},"end":{"row":49,"column":15},"action":"remove","lines":["g"]},{"start":{"row":49,"column":13},"end":{"row":49,"column":14},"action":"remove","lines":["e"]},{"start":{"row":49,"column":12},"end":{"row":49,"column":13},"action":"remove","lines":["t"]},{"start":{"row":49,"column":11},"end":{"row":49,"column":12},"action":"remove","lines":["a"]},{"start":{"row":49,"column":10},"end":{"row":49,"column":11},"action":"remove","lines":["c"]}],[{"start":{"row":49,"column":10},"end":{"row":49,"column":17},"action":"insert","lines":["cuisine"],"id":700}],[{"start":{"row":49,"column":50},"end":{"row":49,"column":51},"action":"remove","lines":["y"],"id":701},{"start":{"row":49,"column":49},"end":{"row":49,"column":50},"action":"remove","lines":["r"]},{"start":{"row":49,"column":48},"end":{"row":49,"column":49},"action":"remove","lines":["o"]},{"start":{"row":49,"column":47},"end":{"row":49,"column":48},"action":"remove","lines":["g"]},{"start":{"row":49,"column":46},"end":{"row":49,"column":47},"action":"remove","lines":["e"]},{"start":{"row":49,"column":45},"end":{"row":49,"column":46},"action":"remove","lines":["t"]},{"start":{"row":49,"column":44},"end":{"row":49,"column":45},"action":"remove","lines":["a"]},{"start":{"row":49,"column":43},"end":{"row":49,"column":44},"action":"remove","lines":["c"]}],[{"start":{"row":49,"column":43},"end":{"row":49,"column":50},"action":"insert","lines":["cuisine"],"id":702}],[{"start":{"row":50,"column":42},"end":{"row":50,"column":43},"action":"remove","lines":["s"],"id":703},{"start":{"row":50,"column":41},"end":{"row":50,"column":42},"action":"remove","lines":["e"]},{"start":{"row":50,"column":40},"end":{"row":50,"column":41},"action":"remove","lines":["i"]},{"start":{"row":50,"column":39},"end":{"row":50,"column":40},"action":"remove","lines":["r"]},{"start":{"row":50,"column":38},"end":{"row":50,"column":39},"action":"remove","lines":["o"]},{"start":{"row":50,"column":37},"end":{"row":50,"column":38},"action":"remove","lines":["g"]},{"start":{"row":50,"column":36},"end":{"row":50,"column":37},"action":"remove","lines":["e"]},{"start":{"row":50,"column":35},"end":{"row":50,"column":36},"action":"remove","lines":["t"]},{"start":{"row":50,"column":34},"end":{"row":50,"column":35},"action":"remove","lines":["a"]},{"start":{"row":50,"column":33},"end":{"row":50,"column":34},"action":"remove","lines":["c"]}],[{"start":{"row":50,"column":33},"end":{"row":50,"column":40},"action":"insert","lines":["cuisine"],"id":704}],[{"start":{"row":38,"column":0},"end":{"row":43,"column":42},"action":"remove","lines":["@app.route('/update_cuisine/<cuisine_id>', methods=['POST'])","def update_cuisine(cuisine_id):","    mongo.db.cuisines.update(","        {'_id': ObjectId(cuisine_id)},","        {'cuisine_name': request.form.get['cuisine_name']})","    return redirect(url_for(get_cuisines))"],"id":705},{"start":{"row":37,"column":0},"end":{"row":38,"column":0},"action":"remove","lines":["",""]},{"start":{"row":36,"column":71},"end":{"row":37,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":39,"column":19},"end":{"row":39,"column":29},"action":"remove","lines":["cuisine_id"],"id":709},{"start":{"row":39,"column":19},"end":{"row":39,"column":29},"action":"insert","lines":["cuisine_id"]}],[{"start":{"row":40,"column":20},"end":{"row":40,"column":21},"action":"insert","lines":["s"],"id":710}],[{"start":{"row":43,"column":40},"end":{"row":43,"column":41},"action":"insert","lines":["s"],"id":711}],[{"start":{"row":43,"column":29},"end":{"row":43,"column":41},"action":"remove","lines":["get_cuisines"],"id":712},{"start":{"row":43,"column":29},"end":{"row":43,"column":30},"action":"insert","lines":["e"]},{"start":{"row":43,"column":30},"end":{"row":43,"column":31},"action":"insert","lines":["d"]}],[{"start":{"row":43,"column":29},"end":{"row":43,"column":31},"action":"remove","lines":["ed"],"id":713},{"start":{"row":43,"column":29},"end":{"row":43,"column":41},"action":"insert","lines":["edit_cuisine"]}],[{"start":{"row":43,"column":40},"end":{"row":43,"column":41},"action":"remove","lines":["e"],"id":720},{"start":{"row":43,"column":39},"end":{"row":43,"column":40},"action":"remove","lines":["n"]},{"start":{"row":43,"column":38},"end":{"row":43,"column":39},"action":"remove","lines":["i"]},{"start":{"row":43,"column":37},"end":{"row":43,"column":38},"action":"remove","lines":["s"]},{"start":{"row":43,"column":36},"end":{"row":43,"column":37},"action":"remove","lines":["i"]},{"start":{"row":43,"column":35},"end":{"row":43,"column":36},"action":"remove","lines":["u"]},{"start":{"row":43,"column":34},"end":{"row":43,"column":35},"action":"remove","lines":["c"]},{"start":{"row":43,"column":33},"end":{"row":43,"column":34},"action":"remove","lines":["_"]},{"start":{"row":43,"column":32},"end":{"row":43,"column":33},"action":"remove","lines":["t"]},{"start":{"row":43,"column":31},"end":{"row":43,"column":32},"action":"remove","lines":["i"]},{"start":{"row":43,"column":30},"end":{"row":43,"column":31},"action":"remove","lines":["d"]},{"start":{"row":43,"column":29},"end":{"row":43,"column":30},"action":"remove","lines":["e"]}],[{"start":{"row":43,"column":29},"end":{"row":43,"column":30},"action":"insert","lines":["g"],"id":721}],[{"start":{"row":43,"column":29},"end":{"row":43,"column":30},"action":"remove","lines":["g"],"id":722},{"start":{"row":43,"column":29},"end":{"row":43,"column":41},"action":"insert","lines":["get_cuisines"]}],[{"start":{"row":43,"column":40},"end":{"row":43,"column":41},"action":"remove","lines":["s"],"id":723}],[{"start":{"row":43,"column":40},"end":{"row":43,"column":41},"action":"insert","lines":["s"],"id":724}],[{"start":{"row":43,"column":29},"end":{"row":43,"column":41},"action":"remove","lines":["get_cuisines"],"id":725},{"start":{"row":43,"column":29},"end":{"row":43,"column":30},"action":"insert","lines":["e"]}],[{"start":{"row":43,"column":30},"end":{"row":43,"column":31},"action":"insert","lines":["d"],"id":726}],[{"start":{"row":43,"column":29},"end":{"row":43,"column":31},"action":"remove","lines":["ed"],"id":727},{"start":{"row":43,"column":29},"end":{"row":43,"column":41},"action":"insert","lines":["edit_cuisine"]}],[{"start":{"row":43,"column":29},"end":{"row":43,"column":41},"action":"remove","lines":["edit_cuisine"],"id":729},{"start":{"row":43,"column":29},"end":{"row":43,"column":30},"action":"insert","lines":["u"]},{"start":{"row":43,"column":30},"end":{"row":43,"column":31},"action":"insert","lines":["p"]}],[{"start":{"row":43,"column":29},"end":{"row":43,"column":31},"action":"remove","lines":["up"],"id":730},{"start":{"row":43,"column":29},"end":{"row":43,"column":43},"action":"insert","lines":["update_cuisine"]}],[{"start":{"row":43,"column":42},"end":{"row":43,"column":43},"action":"remove","lines":["e"],"id":731},{"start":{"row":43,"column":41},"end":{"row":43,"column":42},"action":"remove","lines":["n"]},{"start":{"row":43,"column":40},"end":{"row":43,"column":41},"action":"remove","lines":["i"]},{"start":{"row":43,"column":39},"end":{"row":43,"column":40},"action":"remove","lines":["s"]},{"start":{"row":43,"column":38},"end":{"row":43,"column":39},"action":"remove","lines":["i"]},{"start":{"row":43,"column":37},"end":{"row":43,"column":38},"action":"remove","lines":["u"]},{"start":{"row":43,"column":36},"end":{"row":43,"column":37},"action":"remove","lines":["c"]},{"start":{"row":43,"column":35},"end":{"row":43,"column":36},"action":"remove","lines":["_"]},{"start":{"row":43,"column":34},"end":{"row":43,"column":35},"action":"remove","lines":["e"]},{"start":{"row":43,"column":33},"end":{"row":43,"column":34},"action":"remove","lines":["t"]},{"start":{"row":43,"column":32},"end":{"row":43,"column":33},"action":"remove","lines":["a"]},{"start":{"row":43,"column":31},"end":{"row":43,"column":32},"action":"remove","lines":["d"]},{"start":{"row":43,"column":30},"end":{"row":43,"column":31},"action":"remove","lines":["p"]}],[{"start":{"row":43,"column":29},"end":{"row":43,"column":30},"action":"remove","lines":["u"],"id":732}],[{"start":{"row":43,"column":29},"end":{"row":43,"column":30},"action":"insert","lines":["g"],"id":733}],[{"start":{"row":43,"column":29},"end":{"row":43,"column":30},"action":"remove","lines":["g"],"id":734},{"start":{"row":43,"column":29},"end":{"row":43,"column":41},"action":"insert","lines":["get_cuisines"]}],[{"start":{"row":44,"column":0},"end":{"row":45,"column":0},"action":"insert","lines":["",""],"id":735},{"start":{"row":45,"column":0},"end":{"row":46,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":45,"column":0},"end":{"row":45,"column":1},"action":"insert","lines":["@"],"id":736},{"start":{"row":45,"column":1},"end":{"row":45,"column":2},"action":"insert","lines":["a"]},{"start":{"row":45,"column":2},"end":{"row":45,"column":3},"action":"insert","lines":["p"]},{"start":{"row":45,"column":3},"end":{"row":45,"column":4},"action":"insert","lines":["p"]},{"start":{"row":45,"column":4},"end":{"row":45,"column":5},"action":"insert","lines":["."]},{"start":{"row":45,"column":5},"end":{"row":45,"column":6},"action":"insert","lines":["r"]},{"start":{"row":45,"column":6},"end":{"row":45,"column":7},"action":"insert","lines":["p"]}],[{"start":{"row":45,"column":6},"end":{"row":45,"column":7},"action":"remove","lines":["p"],"id":737}],[{"start":{"row":45,"column":6},"end":{"row":45,"column":7},"action":"insert","lines":["o"],"id":738},{"start":{"row":45,"column":7},"end":{"row":45,"column":8},"action":"insert","lines":["u"]},{"start":{"row":45,"column":8},"end":{"row":45,"column":9},"action":"insert","lines":["t"]},{"start":{"row":45,"column":9},"end":{"row":45,"column":10},"action":"insert","lines":["e"]}],[{"start":{"row":45,"column":5},"end":{"row":45,"column":10},"action":"remove","lines":["route"],"id":739},{"start":{"row":45,"column":5},"end":{"row":45,"column":12},"action":"insert","lines":["route()"]}],[{"start":{"row":45,"column":11},"end":{"row":45,"column":13},"action":"insert","lines":["''"],"id":740}],[{"start":{"row":45,"column":12},"end":{"row":45,"column":13},"action":"insert","lines":["/"],"id":741},{"start":{"row":45,"column":13},"end":{"row":45,"column":14},"action":"insert","lines":["d"]},{"start":{"row":45,"column":14},"end":{"row":45,"column":15},"action":"insert","lines":["e"]},{"start":{"row":45,"column":15},"end":{"row":45,"column":16},"action":"insert","lines":["l"]},{"start":{"row":45,"column":16},"end":{"row":45,"column":17},"action":"insert","lines":["e"]}],[{"start":{"row":45,"column":13},"end":{"row":45,"column":17},"action":"remove","lines":["dele"],"id":742},{"start":{"row":45,"column":13},"end":{"row":45,"column":27},"action":"insert","lines":["delete_cuisine"]}],[{"start":{"row":45,"column":27},"end":{"row":45,"column":28},"action":"insert","lines":["/"],"id":743},{"start":{"row":45,"column":28},"end":{"row":45,"column":29},"action":"insert","lines":["<"]},{"start":{"row":45,"column":29},"end":{"row":45,"column":30},"action":"insert","lines":["c"]},{"start":{"row":45,"column":30},"end":{"row":45,"column":31},"action":"insert","lines":["u"]}],[{"start":{"row":45,"column":29},"end":{"row":45,"column":31},"action":"remove","lines":["cu"],"id":744},{"start":{"row":45,"column":29},"end":{"row":45,"column":39},"action":"insert","lines":["cuisine_id"]}],[{"start":{"row":45,"column":39},"end":{"row":45,"column":40},"action":"insert","lines":[">"],"id":745}],[{"start":{"row":45,"column":42},"end":{"row":46,"column":0},"action":"insert","lines":["",""],"id":746},{"start":{"row":46,"column":0},"end":{"row":46,"column":1},"action":"insert","lines":["d"]},{"start":{"row":46,"column":1},"end":{"row":46,"column":2},"action":"insert","lines":["e"]},{"start":{"row":46,"column":2},"end":{"row":46,"column":3},"action":"insert","lines":["f"]}],[{"start":{"row":46,"column":3},"end":{"row":46,"column":4},"action":"insert","lines":[" "],"id":747},{"start":{"row":46,"column":4},"end":{"row":46,"column":5},"action":"insert","lines":["d"]},{"start":{"row":46,"column":5},"end":{"row":46,"column":6},"action":"insert","lines":["e"]}],[{"start":{"row":46,"column":6},"end":{"row":46,"column":7},"action":"insert","lines":["l"],"id":748}],[{"start":{"row":46,"column":4},"end":{"row":46,"column":7},"action":"remove","lines":["del"],"id":749},{"start":{"row":46,"column":4},"end":{"row":46,"column":18},"action":"insert","lines":["delete_cuisine"]}],[{"start":{"row":46,"column":18},"end":{"row":46,"column":20},"action":"insert","lines":["()"],"id":750}],[{"start":{"row":46,"column":19},"end":{"row":46,"column":20},"action":"insert","lines":["c"],"id":751},{"start":{"row":46,"column":20},"end":{"row":46,"column":21},"action":"insert","lines":["u"]}],[{"start":{"row":46,"column":19},"end":{"row":46,"column":21},"action":"remove","lines":["cu"],"id":752},{"start":{"row":46,"column":19},"end":{"row":46,"column":29},"action":"insert","lines":["cuisine_id"]}],[{"start":{"row":46,"column":30},"end":{"row":46,"column":31},"action":"insert","lines":[":"],"id":753}],[{"start":{"row":46,"column":31},"end":{"row":47,"column":0},"action":"insert","lines":["",""],"id":754},{"start":{"row":47,"column":0},"end":{"row":47,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":47,"column":4},"end":{"row":47,"column":5},"action":"insert","lines":["m"],"id":755},{"start":{"row":47,"column":5},"end":{"row":47,"column":6},"action":"insert","lines":["o"]},{"start":{"row":47,"column":6},"end":{"row":47,"column":7},"action":"insert","lines":["n"]},{"start":{"row":47,"column":7},"end":{"row":47,"column":8},"action":"insert","lines":["g"]},{"start":{"row":47,"column":8},"end":{"row":47,"column":9},"action":"insert","lines":["o"]},{"start":{"row":47,"column":9},"end":{"row":47,"column":10},"action":"insert","lines":["."]}],[{"start":{"row":47,"column":10},"end":{"row":47,"column":11},"action":"insert","lines":["d"],"id":756},{"start":{"row":47,"column":11},"end":{"row":47,"column":12},"action":"insert","lines":["b"]},{"start":{"row":47,"column":12},"end":{"row":47,"column":13},"action":"insert","lines":["."]},{"start":{"row":47,"column":13},"end":{"row":47,"column":14},"action":"insert","lines":["c"]}],[{"start":{"row":47,"column":14},"end":{"row":47,"column":15},"action":"insert","lines":["u"],"id":757},{"start":{"row":47,"column":15},"end":{"row":47,"column":16},"action":"insert","lines":["i"]}],[{"start":{"row":47,"column":13},"end":{"row":47,"column":16},"action":"remove","lines":["cui"],"id":758},{"start":{"row":47,"column":13},"end":{"row":47,"column":21},"action":"insert","lines":["cuisines"]}],[{"start":{"row":47,"column":21},"end":{"row":47,"column":22},"action":"insert","lines":["."],"id":759}],[{"start":{"row":47,"column":22},"end":{"row":47,"column":23},"action":"insert","lines":["r"],"id":760},{"start":{"row":47,"column":23},"end":{"row":47,"column":24},"action":"insert","lines":["e"]},{"start":{"row":47,"column":24},"end":{"row":47,"column":25},"action":"insert","lines":["m"]},{"start":{"row":47,"column":25},"end":{"row":47,"column":26},"action":"insert","lines":["o"]},{"start":{"row":47,"column":26},"end":{"row":47,"column":27},"action":"insert","lines":["v"]},{"start":{"row":47,"column":27},"end":{"row":47,"column":28},"action":"insert","lines":["e"]}],[{"start":{"row":47,"column":28},"end":{"row":47,"column":30},"action":"insert","lines":["()"],"id":761}],[{"start":{"row":47,"column":29},"end":{"row":47,"column":31},"action":"insert","lines":["{}"],"id":762}],[{"start":{"row":47,"column":30},"end":{"row":47,"column":31},"action":"insert","lines":[";"],"id":763}],[{"start":{"row":47,"column":31},"end":{"row":47,"column":32},"action":"insert","lines":["i"],"id":764},{"start":{"row":47,"column":32},"end":{"row":47,"column":33},"action":"insert","lines":["d"]},{"start":{"row":47,"column":33},"end":{"row":47,"column":34},"action":"insert","lines":["_"]}],[{"start":{"row":47,"column":33},"end":{"row":47,"column":34},"action":"remove","lines":["_"],"id":765},{"start":{"row":47,"column":32},"end":{"row":47,"column":33},"action":"remove","lines":["d"]},{"start":{"row":47,"column":31},"end":{"row":47,"column":32},"action":"remove","lines":["i"]},{"start":{"row":47,"column":30},"end":{"row":47,"column":31},"action":"remove","lines":[";"]}],[{"start":{"row":47,"column":30},"end":{"row":47,"column":32},"action":"insert","lines":["''"],"id":766}],[{"start":{"row":47,"column":31},"end":{"row":47,"column":32},"action":"insert","lines":["_"],"id":767},{"start":{"row":47,"column":32},"end":{"row":47,"column":33},"action":"insert","lines":["i"]},{"start":{"row":47,"column":33},"end":{"row":47,"column":34},"action":"insert","lines":["d"]}],[{"start":{"row":47,"column":35},"end":{"row":47,"column":36},"action":"insert","lines":[":"],"id":768}],[{"start":{"row":47,"column":36},"end":{"row":47,"column":37},"action":"insert","lines":[" "],"id":769},{"start":{"row":47,"column":37},"end":{"row":47,"column":38},"action":"insert","lines":["O"]},{"start":{"row":47,"column":38},"end":{"row":47,"column":39},"action":"insert","lines":["b"]}],[{"start":{"row":47,"column":37},"end":{"row":47,"column":39},"action":"remove","lines":["Ob"],"id":770},{"start":{"row":47,"column":37},"end":{"row":47,"column":45},"action":"insert","lines":["ObjectId"]}],[{"start":{"row":47,"column":45},"end":{"row":47,"column":47},"action":"insert","lines":["()"],"id":771}],[{"start":{"row":47,"column":46},"end":{"row":47,"column":47},"action":"insert","lines":["c"],"id":772},{"start":{"row":47,"column":47},"end":{"row":47,"column":48},"action":"insert","lines":["u"]}],[{"start":{"row":47,"column":46},"end":{"row":47,"column":48},"action":"remove","lines":["cu"],"id":773},{"start":{"row":47,"column":46},"end":{"row":47,"column":56},"action":"insert","lines":["cuisine_id"]}],[{"start":{"row":47,"column":58},"end":{"row":47,"column":59},"action":"insert","lines":[","],"id":774}],[{"start":{"row":47,"column":59},"end":{"row":48,"column":0},"action":"insert","lines":["",""],"id":775},{"start":{"row":48,"column":0},"end":{"row":48,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":48,"column":4},"end":{"row":48,"column":5},"action":"insert","lines":["r"],"id":776},{"start":{"row":48,"column":5},"end":{"row":48,"column":6},"action":"insert","lines":["e"]}],[{"start":{"row":48,"column":6},"end":{"row":48,"column":7},"action":"insert","lines":["t"],"id":777},{"start":{"row":48,"column":7},"end":{"row":48,"column":8},"action":"insert","lines":["u"]},{"start":{"row":48,"column":8},"end":{"row":48,"column":9},"action":"insert","lines":["r"]},{"start":{"row":48,"column":9},"end":{"row":48,"column":10},"action":"insert","lines":["n"]}],[{"start":{"row":48,"column":10},"end":{"row":48,"column":11},"action":"insert","lines":[" "],"id":778},{"start":{"row":48,"column":11},"end":{"row":48,"column":12},"action":"insert","lines":["r"]},{"start":{"row":48,"column":12},"end":{"row":48,"column":13},"action":"insert","lines":["e"]}],[{"start":{"row":48,"column":11},"end":{"row":48,"column":13},"action":"remove","lines":["re"],"id":779},{"start":{"row":48,"column":11},"end":{"row":48,"column":21},"action":"insert","lines":["redirect()"]}],[{"start":{"row":48,"column":20},"end":{"row":48,"column":21},"action":"insert","lines":["u"],"id":780},{"start":{"row":48,"column":21},"end":{"row":48,"column":22},"action":"insert","lines":["r"]}],[{"start":{"row":48,"column":20},"end":{"row":48,"column":22},"action":"remove","lines":["ur"],"id":781},{"start":{"row":48,"column":20},"end":{"row":48,"column":29},"action":"insert","lines":["url_for()"]}],[{"start":{"row":48,"column":28},"end":{"row":48,"column":29},"action":"insert","lines":["g"],"id":782},{"start":{"row":48,"column":29},"end":{"row":48,"column":30},"action":"insert","lines":["e"]}],[{"start":{"row":48,"column":29},"end":{"row":48,"column":30},"action":"remove","lines":["e"],"id":783},{"start":{"row":48,"column":28},"end":{"row":48,"column":29},"action":"remove","lines":["g"]}],[{"start":{"row":48,"column":28},"end":{"row":48,"column":30},"action":"insert","lines":["''"],"id":784}],[{"start":{"row":48,"column":29},"end":{"row":48,"column":30},"action":"insert","lines":["g"],"id":785},{"start":{"row":48,"column":30},"end":{"row":48,"column":31},"action":"insert","lines":["e"]}],[{"start":{"row":48,"column":29},"end":{"row":48,"column":31},"action":"remove","lines":["ge"],"id":786},{"start":{"row":48,"column":29},"end":{"row":48,"column":41},"action":"insert","lines":["get_cuisines"]}],[{"start":{"row":47,"column":58},"end":{"row":47,"column":59},"action":"insert","lines":[")"],"id":787}],[{"start":{"row":48,"column":44},"end":{"row":48,"column":45},"action":"remove","lines":[")"],"id":788}]]},"ace":{"folds":[],"scrolltop":420,"scrollleft":0,"selection":{"start":{"row":48,"column":44},"end":{"row":48,"column":44},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":3,"state":"start","mode":"ace/mode/python"}},"timestamp":1564603679116,"hash":"2815552eba375b065a4314a0f828465f18f4a1b9"}