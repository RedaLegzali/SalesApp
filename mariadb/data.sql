insert into channels (name)
values
	("USA"),
	("CAN"),
	("FRA");

insert into nodes (name)
values
	("Decoration"),
	("Furnitures"),
	("Kitchenware");

insert into channels_nodes (channel_id,node_id)
values
	(1,1),
	(1,2),
	(1,3),
	(2,1),
	(2,2),
	(3,1),
	(3,3);

insert into products (name,image,node_id)
values
	("Mirrors","mirrors.jpg",1),
	("Clocks","clocks.jpg",1),
	("Vases","vases.jpg",1),
	("Tables","tables.jpg",2),
	("Chairs","chairs.jpg",2),
	("Sofas","sofas.jpg",2),
	("Cookware","cookware.jpg",3),
	("Cutlery","cutlery.jpg",3),
	("Serveware","serveware.jpg",3);

insert into skus (name,quantity,price,promotion,image,product_id)
values
	("Large Round Mirror 70cm x 70cm",100,89.95,default,"large_round_mirror.jpg",1),
	("Tall Gold Wall Mirror 42cm x 156cm",0,230.95,0.25,"tall_wall_mirror.jpg",1),
	("Round Silver Mirror 68cm x 68cm",50,80.95,default,"round_silver_mirror.jpg",1),
	("Extra Large Silver Skeleton Wall Clock",120,95.95,default,"large_silver_clock.jpg",2),
	("Vintage Distressed Mantel Clock",25,52.95,default,"vintage_mantel_clock.jpg",2),
	("Large Black and Gold Skeleton Wall Clock",0,130.95,0.20,"large_black_gold_wall_clock.jpg",2),
	("Small Grey Glass Dimple Vase",0,4.95,default,"small_grey_vase.jpg",3),
	("Tall Clear Glass Daisy Vase",30,22.95,default,"tall_glass_vase.jpg",3),
	("Green Glass Daisy Vase",40,22.95,default,"green_glass_vase.jpg",3),
	("Rustic Wooden Tripod Side Table",0,109.95,default,"rustic_tripod_table.jpg",4),
	("Large Wooden Nordic Dining Table",25,1766.95,0.50,"large_nordic_table.jpg",4),
	("White Metal Wire Basket Wooden Top Side Table",40,25.95,default,"white_basket_table.jpg",4),
	("Cream Wooden Rattan Dining Chair",35,154.95,0.20,"cream_wooden_chair.jpg",5),
	("Wood & Metal Folding Chair",40,144.95,default,"wood_metal_chair.jpg",5),
	("Orange & Gold Ribbed Velvet Chair",0,553.95,0.25,"gold_velvet_chair.jpg",5),
	("Large Green Velvet Chesterfield Sofa",10,1489.95,0.50,"large_green_sofa.jpg",6),
	("Large Grey Velvet 2 Seater Sofa",15,1068.95,0.25,"large_grey_sofa.jpg",6),
	("Lodge Chef Collection Seasoned Cast Iron Skillet",40,30.95,default,"lodge_chef_skillet.jpg",7),
	("Le Creuset Graphite Dutch Oven",25,340.95,0.25,"creuset_oven.jpg",7),
	("7-Piece In-Drawer Knife Set",30,220.95,0.20,"seven_knife_set.jpg",8),
	("6-Piece Carbon Steel Wok Set",0,60.95,default,"carbon_wok.jpg",8),
	("10-Piece Steak and Carving Knives Set",35,120.95,default,"ten_knife_set.jpg",8),
	("Ikon Steak Knives Set of 4",20,235.95,0.30,"steak_knife_set.jpg",8),
	("Oven-to-Table Two-Part Dish with Trivet",30,300.95,0.30,"oven_table_dish.jpg",9),
	("Tondo 5.75 Bowl",0,6.95,default,"tondo.jpg",9),
	("Gold Cheese Knives Set of 3",100,22.95,default,"gold_cheese_knives.jpg",9);

