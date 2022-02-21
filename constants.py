log_in_link = 'https://twitter.com/i/flow/login'
email = 'pharmacyisa6@gmail.com'
username = '@IsaPharmacy'
password = 'tim12isaprojekat'

queries = {
    'kosovo':
        ['kosovo (from:avucic OR from:adv_djukanovic OR from:SerbianPM OR from:TomaMomirovic OR from:Nevena_Djuric93 OR from:AcaSapic OR from:ZoranT11 OR from:Vladimir_Orlic OR from:VucevicM OR from:markodjuric OR from:NesaStefanovic OR from:MarijanNSS OR from:Jakssa077 OR from:VjericaR OR from:AlekSeselj OR from:NemanjaSarovic OR from:BoskoObradovic OR from:SPDveri OR from:NovaStranka OR from:ArisMovsesijan OR from:demokrate OR from:ZoranLutovac OR from:SutanovacDragan OR from:PartizanusV)',
         'kosovo (from:DostaJeBilo OR from:SasaRadulovich OR from:BiljicVojin OR from:hanaadrovic OR from:SlobodaIPravda OR from:DraganDjilas OR from:BorkoStef OR from:MarinikaTepic OR from:DanijelaGruji2 OR from:ZdravkoPonos OR from:WhistlerDick OR from:niinochka OR from:anna_bubisha OR from:StrankaNarodna OR from:jeremic_vuk OR from:MiikiAleksic)'
        ]
}

# (x,y) => (economic policy [-1 {Left}, 1 {Right}], social policy [-1 {Libertarian}, 1 {Authoritarian}]) [-1, 0.1, 1]
accountMap = {
    '@avucic' : (0.6, 0.8),
    '@adv_djukanovic' : (0.8, 0.9),
    '@SerbianPM' : (0.1, 0.5),
    '@TomaMomirovic' : (0.1, 0.4),
    '@Nevena_Djuric93' : (0.3, 0.9),
    '@AcaSapic' : (0.0, 0.4),
    '@ZoranT11' : (0.5, 0.7),
    '@Vladimir_Orlic' : (0.4, 0.8),
    '@VucevicM' : (0.2, 0.9),
    '@markodjuric' : (0.3, 0.9),
    '@NesaStefanovic' : (0.5, 0.8),
    '@MarijanNSS' : (0.4, 0.8),
    '@socijalisti' : (-0.8, 0.8),
    '@Jakssa077' : (0.8, 1),
    '@VjericaR' : (0.7, 1),
    '@AlekSeselj' : (0.8, 0.7),
    '@NemanjaSarovic' : (0.7, 0.4),
    '@BoskoObradovic' : (0.4, 0.8),
    '@SPDveri' : (0.3, 0.8),
    '@NovaStranka' : (0.4, -0.5),
    '@ArisMovsesijan' : (0.3, -0.6),
    '@demokrate' : (0.4, -0.7),
    '@ZoranLutovac' : (0.3, -0.2),
    '@SutanovacDragan' : (0.4, -0.1),
    '@PartizanusV' : (0.3, 0.5),
    '@SasaRadulovic' : (0.2, 0.6),
    '@BiljicVojin' : (0.3, 0.7),
    '@hanaadrovic' : (0.4, 0.4),
    '@DraganDjilas' : (0.3, -0.5),
    '@BorkoStef' : (0.1, -0.3),
    '@MarinikaTepic' : (0.1, -0.4),
    '@DanijelaGruji2' : (0, -0.7),
    '@ZdravkoPonos' : (0.3, 0.5),
    '@WhistlerDick' : (0.1, -1),
    '@niinochka' : (0, 1),
    '@anna_bubisha' : (0.1, -0.8) ,
    '@StrankaNarodna' : (-0.2, -0.7),
    '@jeremic_vuk' : (0, -0.2),
    '@MiikiAleksic' : (0.2, 0.2),
    '@XXLTulip' : (-0.9, 1),
    '@BorisTadic58' : (0.3, 0.6)
    '@brankoruzicsps' : (-0.7, 0.6),
    '@AAnticBG' : (-0.8, 0.5)
}