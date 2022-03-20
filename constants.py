log_in_link = 'https://twitter.com/i/flow/login'
email = 'pharmacyisa6@gmail.com'
username = '@IsaPharmacy'
password = 'tim12isaprojekat'
accountMap = {
    '@avucic': (0.6, 0.8),
    '@adv_djukanovic': (0.8, 0.9),
    '@SerbianPM': (0.1, 0.5),
    '@TomaMomirovic': (0.1, 0.4),
    '@Nevena_Djuric93': (0.3, 0.9),
    '@AcaSapic': (0.0, 0.4),
    '@ZoranT11': (0.5, 0.7),
    '@Vladimir_Orlic': (0.4, 0.8),
    '@VucevicM': (0.2, 0.9),
    '@markodjuric': (0.3, 0.9),
    '@NesaStefanovic': (0.5, 0.8),
    '@MarijanNSS': (0.4, 0.8),
    '@socijalisti': (-0.8, 0.8),
    '@Jakssa077': (0.8, 1),
    '@VjericaR': (0.7, 1),
    '@AlekSeselj': (0.8, 0.7),
    '@NemanjaSarovic': (0.7, 0.4),
    '@BoskoObradovic': (0.4, 0.8),
    '@SPDveri': (0.3, 0.8),
    '@NovaStranka': (0.4, -0.5),
    '@ArisMovsesijan': (0.3, -0.6),
    '@demokrate': (0.4, -0.7),
    '@ZoranLutovac': (0.3, -0.2),
    '@SutanovacDragan': (0.4, -0.1),
    '@PartizanusV': (0.3, 0.5),
    '@SasaRadulovich': (0.2, 0.6),
    '@DostaJeBilo': (0.2, 0.6),
    '@BiljicVojin': (0.3, 0.7),
    '@hanaadrovic': (0.4, 0.4),
    '@SlobodaIPravda': (-0.5, 0),
    '@DraganDjilas': (0.3, -0.5),
    '@BorkoStef': (0.1, -0.3),
    '@MarinikaTepic': (0.1, -0.4),
    '@DanijelaGruji2': (0, -0.7),
    '@ZdravkoPonos': (0.3, 0.5),
    '@WhistlerDick': (0.1, -1),
    '@niinochka': (0, 1),
    '@anna_bubisha': (0.1, -0.8),
    '@StrankaNarodna': (-0.2, -0.7),
    '@jeremic_vuk': (0, -0.2),
    '@MiikiAleksic': (0.2, 0.2),
    '@XXLTulip': (-0.9, 1),
    '@BorisTadic58': (0.3, 0.6),
    '@brankoruzicsps': (-0.7, 0.6),
    '@AAnticBG': (-0.8, 0.5),
    # 
    '@BrajanBrkovic': (-1, 0.5),
    '@MiranPogacar': (-0.9, -0.1),
    '@P_Socijalista': (-0.8, 1),
    '@nedavimobgd': (-0.3, 0),
    '@partijarada': (-0.7, 0.5),
    '@ZelenaStrankaRS': (-0.3, -0.4),
    '@FantomiSRB': (-0.7, -0.7),
    '@NKPJ_Srbija': (-1, 1),
    '@skoj_official': (-1, 1),
    '@Ceda_Jovanovic': (-0.2, 1),
    '@LDP': ( -0.3, -0.9),
    '@branislav_lecic': (-0.1, 0.4),
    '@FHPHLC': (0, -0.9),
    '@OsfSerbia': (-0.1, -0.7),
    '@VPartija': (-0.5, 0.5),
    '@Katalonka4': (-0.6, 0.3),
    '@ZajednoZaSrbiju': (-0.4, 0.3),
    '@MORAMO2022': (-0.4, 0.3),
    '@NoviPlamen': (-0.9, 0.4)
}

queries = {
    'kosovo':
        [
            '(косово OR косова OR косову OR косовској OR косовска OR косовски OR kosovo OR kosova OR kosovu OR kosovskoj OR kosovska OR kosovski) (from:avucic OR from:adv_djukanovic OR from:SerbianPM OR from:TomaMomirovic OR from:Nevena_Djuric93 OR from:AcaSapic OR from:ZoranT11 OR from:Vladimir_Orlic OR from:VucevicM OR from:markodjuric OR from:NesaStefanovic OR from:MarijanNSS OR from:Jakssa077 OR from:VjericaR OR from:AlekSeselj OR from:NemanjaSarovic)',
            '(косово OR косова OR косову OR косовској OR косовска OR косовски OR kosovo OR kosova OR kosovu OR kosovskoj OR kosovska OR kosovski) (from:BoskoObradovic OR from:SPDveri OR from:NovaStranka OR from:ArisMovsesijan OR from:demokrate OR from:ZoranLutovac OR from:SutanovacDragan OR from:PartizanusV OR from:DostaJeBilo OR from:SasaRadulovich OR from:BiljicVojin OR from:hanaadrovic)',
            '(косово OR косова OR косову OR косовској OR косовска OR косовски OR kosovo OR kosova OR kosovu OR kosovskoj OR kosovska OR kosovski) (from:SlobodaIPravda OR from:DraganDjilas OR from:BorkoStef OR from:MarinikaTepic OR from:DanijelaGruji2 OR from:ZdravkoPonos OR from:WhistlerDick OR from:niinochka OR from:anna_bubisha OR from:StrankaNarodna OR from:jeremic_vuk OR from:MiikiAleksic)',
        ],
    'albanija':
        [
            '(albanci OR albancima OR albanski OR albanskoj OR albanske OR albanija OR albaniju OR albaniji OR албанци OR албанцима OR албански OR албанској OR албанске OR албанија OR албанију OR албанији) (from:avucic OR from:adv_djukanovic OR from:SerbianPM OR from:TomaMomirovic OR from:Nevena_Djuric93 OR from:AcaSapic OR from:ZoranT11 OR from:Vladimir_Orlic OR from:VucevicM OR from:markodjuric OR from:NesaStefanovic OR from:MarijanNSS OR from:Jakssa077 OR from:VjericaR OR from:AlekSeselj)',
            '(albanci OR albancima OR albanski OR albanskoj OR albanske OR albanija OR albaniju OR albaniji OR албанци OR албанцима OR албански OR албанској OR албанске OR албанија OR албанију OR албанији) (from:BoskoObradovic OR from:SPDveri OR from:NovaStranka OR from:ArisMovsesijan OR from:demokrate OR from:ZoranLutovac OR from:SutanovacDragan OR from:PartizanusV OR from:DostaJeBilo OR from:SasaRadulovich OR from:BiljicVojin OR from:hanaadrovic OR from:NemanjaSarovic)',
            '(albanci OR albancima OR albanski OR albanskoj OR albanske OR albanija OR albaniju OR albaniji OR албанци OR албанцима OR албански OR албанској OR албанске OR албанија OR албанију OR албанији) (from:SlobodaIPravda OR from:DraganDjilas OR from:BorkoStef OR from:MarinikaTepic OR from:DanijelaGruji2 OR from:ZdravkoPonos OR from:WhistlerDick OR from:niinochka OR from:anna_bubisha OR from:StrankaNarodna OR from:jeremic_vuk OR from:MiikiAleksic)',
        ],
    'vojska':
        [
            '(vojska OR vojsci OR vojske OR vojna OR vojni OR војска OR војсци OR војске OR војна OR војни) (from:avucic OR from:adv_djukanovic OR from:SerbianPM OR from:TomaMomirovic OR from:Nevena_Djuric93 OR from:AcaSapic OR from:ZoranT11 OR from:Vladimir_Orlic OR from:VucevicM OR from:markodjuric OR from:NesaStefanovic OR from:MarijanNSS OR from:Jakssa077 OR from:VjericaR OR from:AlekSeselj OR from:NemanjaSarovic)',
            '(vojska OR vojsci OR vojske OR vojna OR vojni OR војска OR војсци OR војске OR војна OR војни) (from:BoskoObradovic OR from:SPDveri OR from:NovaStranka OR from:ArisMovsesijan OR from:demokrate OR from:ZoranLutovac OR from:SutanovacDragan OR from:PartizanusV OR from:DostaJeBilo OR from:SasaRadulovich OR from:BiljicVojin OR from:hanaadrovic)',
            '(vojska OR vojsci OR vojske OR vojna OR vojni OR војска OR војсци OR војске OR војна OR војни) (from:SlobodaIPravda OR from:DraganDjilas OR from:BorkoStef OR from:MarinikaTepic OR from:DanijelaGruji2 OR from:ZdravkoPonos OR from:WhistlerDick OR from:niinochka OR from:anna_bubisha OR from:StrankaNarodna OR from:jeremic_vuk OR from:MiikiAleksic)',
        ],
    'crkva':
        [
            '(crkva OR crkvi OR crkve OR crkveni OR pravoslavlje OR pravoslavni OR pravoslavlja OR pravoslavno OR црква OR цркви OR цркве OR црквени OR православље OR православни OR православља OR православно) (from:avucic OR from:adv_djukanovic OR from:SerbianPM OR from:TomaMomirovic OR from:Nevena_Djuric93 OR from:AcaSapic OR from:ZoranT11 OR from:Vladimir_Orlic OR from:VucevicM OR from:markodjuric OR from:NesaStefanovic OR from:MarijanNSS OR from:Jakssa077 OR from:VjericaR OR from:AlekSeselj)',
            '(crkva OR crkvi OR crkve OR crkveni OR pravoslavlje OR pravoslavni OR pravoslavlja OR pravoslavno OR црква OR цркви OR цркве OR црквени OR православље OR православни OR православља OR православно) (from:BoskoObradovic OR from:SPDveri OR from:NovaStranka OR from:ArisMovsesijan OR from:demokrate OR from:ZoranLutovac OR from:SutanovacDragan OR from:PartizanusV OR from:DostaJeBilo OR from:SasaRadulovich OR from:BiljicVojin OR from:hanaadrovic OR from:NemanjaSarovic)',
            '(crkva OR crkvi OR crkve OR crkveni OR pravoslavlje OR pravoslavni OR pravoslavlja OR pravoslavno OR црква OR цркви OR цркве OR црквени OR православље OR православни OR православља OR православно) (from:SlobodaIPravda OR from:DraganDjilas OR from:BorkoStef OR from:MarinikaTepic OR from:DanijelaGruji2 OR from:ZdravkoPonos OR from:WhistlerDick OR from:niinochka OR from:anna_bubisha OR from:StrankaNarodna OR from:jeremic_vuk OR from:MiikiAleksic)',
        ],
    'lgbt':
        [
            '(lgbt OR pride OR parada OR ponosa OR paradi OR парада OR параде OR поноса) -vojna -vojne -vojnoj -војна -војне -војној (from:avucic OR from:adv_djukanovic OR from:SerbianPM OR from:TomaMomirovic OR from:Nevena_Djuric93 OR from:AcaSapic OR from:ZoranT11 OR from:Vladimir_Orlic OR from:VucevicM OR from:markodjuric OR from:NesaStefanovic OR from:MarijanNSS OR from:Jakssa077 OR from:VjericaR OR from:AlekSeselj OR from:NemanjaSarovic)',
            '(lgbt OR pride OR parada OR ponosa OR paradi OR парада OR параде OR поноса) -vojna -vojne -vojnoj -војна -војне -војној (from:BoskoObradovic OR from:SPDveri OR from:NovaStranka OR from:ArisMovsesijan OR from:demokrate OR from:ZoranLutovac OR from:SutanovacDragan OR from:PartizanusV OR from:DostaJeBilo OR from:SasaRadulovich OR from:BiljicVojin OR from:hanaadrovic)',
            '(lgbt OR pride OR parada OR ponosa OR paradi OR парада OR параде OR поноса) -vojna -vojne -vojnoj  -војна -војне -војној (from:SlobodaIPravda OR from:DraganDjilas OR from:BorkoStef OR from:MarinikaTepic OR from:DanijelaGruji2 OR from:ZdravkoPonos OR from:WhistlerDick OR from:niinochka OR from:anna_bubisha OR from:StrankaNarodna OR from:jeremic_vuk OR from:MiikiAleksic)',
        ],
    'beograd':
        [
            '(beograd OR beograda OR beogradu OR beogradski OR beogradskom OR београд OR београда OR београду OR београдски OR београдском) (from:avucic OR from:adv_djukanovic OR from:SerbianPM OR from:TomaMomirovic OR from:Nevena_Djuric93 OR from:AcaSapic OR from:ZoranT11 OR from:Vladimir_Orlic OR from:VucevicM OR from:markodjuric OR from:NesaStefanovic OR from:MarijanNSS OR from:Jakssa077 OR from:VjericaR OR from:AlekSeselj OR from:NemanjaSarovic)',
            '(beograd OR beograda OR beogradu OR beogradski OR beogradskom OR београд OR београда OR београду OR београдски OR београдском) (from:BoskoObradovic OR from:SPDveri OR from:NovaStranka OR from:ArisMovsesijan OR from:demokrate OR from:ZoranLutovac OR from:SutanovacDragan OR from:PartizanusV OR from:DostaJeBilo OR from:SasaRadulovich OR from:BiljicVojin OR from:hanaadrovic)',
            '(beograd OR beograda OR beogradu OR beogradski OR beogradskom OR београд OR београда OR београду OR београдски OR београдском) (from:SlobodaIPravda OR from:DraganDjilas OR from:BorkoStef OR from:MarinikaTepic OR from:DanijelaGruji2 OR from:ZdravkoPonos OR from:WhistlerDick OR from:niinochka OR from:anna_bubisha OR from:StrankaNarodna OR from:jeremic_vuk OR from:MiikiAleksic)',
        ],
    'policija':
        [
            '(policija OR policiji OR policije OR policijska OR policijskoj OR milicija OR miliciji OR milicijie OR полиција OR полицији OR полиције OR полицијска OR полицијској OR милиција OR милицији OR милиције) (from:avucic OR from:adv_djukanovic OR from:SerbianPM OR from:TomaMomirovic OR from:Nevena_Djuric93 OR from:AcaSapic OR from:ZoranT11 OR from:Vladimir_Orlic OR from:VucevicM OR from:markodjuric OR from:NesaStefanovic OR from:MarijanNSS OR from:Jakssa077 OR from:VjericaR)',
            '(policija OR policiji OR policije OR policijska OR policijskoj OR milicija OR miliciji OR milicijie OR полиција OR полицији OR полиције OR полицијска OR полицијској OR милиција OR милицији OR милиције) (from:BoskoObradovic OR from:SPDveri OR from:NovaStranka OR from:ArisMovsesijan OR from:demokrate OR from:ZoranLutovac OR from:SutanovacDragan OR from:PartizanusV OR from:DostaJeBilo OR from:SasaRadulovich OR from:BiljicVojin OR from:hanaadrovic OR from:AlekSeselj)',
            '(policija OR policiji OR policije OR policijska OR policijskoj OR milicija OR miliciji OR milicijie OR полиција OR полицији OR полиције OR полицијска OR полицијској OR милиција OR милицији OR милиције) (from:SlobodaIPravda OR from:DraganDjilas OR from:BorkoStef OR from:MarinikaTepic OR from:DanijelaGruji2 OR from:ZdravkoPonos OR from:WhistlerDick OR from:niinochka OR from:anna_bubisha OR from:StrankaNarodna OR from:jeremic_vuk OR from:MiikiAleksic OR from:NemanjaSarovic)',
        ],
    'korupcija':
        [
            '(корупција OR корупцији OR корумпиран OR korupcija OR korupciji OR korumpiran) (from:avucic OR from:adv_djukanovic OR from:SerbianPM OR from:TomaMomirovic OR from:Nevena_Djuric93 OR from:AcaSapic OR from:ZoranT11 OR from:Vladimir_Orlic OR from:VucevicM OR from:markodjuric OR from:NesaStefanovic OR from:MarijanNSS OR from:Jakssa077 OR from:VjericaR OR from:AlekSeselj OR from:NemanjaSarovic)',
            '(корупција OR корупцији OR корумпиран OR korupcija OR korupciji OR korumpiran) (from:BoskoObradovic OR from:SPDveri OR from:NovaStranka OR from:ArisMovsesijan OR from:demokrate OR from:ZoranLutovac OR from:SutanovacDragan OR from:PartizanusV OR from:DostaJeBilo OR from:SasaRadulovich OR from:BiljicVojin OR from:hanaadrovic)',
            '(корупција OR корупцији OR корумпиран OR korupcija OR korupciji OR korumpiran) (from:SlobodaIPravda OR from:DraganDjilas OR from:BorkoStef OR from:MarinikaTepic OR from:DanijelaGruji2 OR from:ZdravkoPonos OR from:WhistlerDick OR from:niinochka OR from:anna_bubisha OR from:StrankaNarodna OR from:jeremic_vuk OR from:MiikiAleksic)',
        ],
    'evropa':
        [
            '(evropa OR evropi OR evropu OR evropska OR evropskoj OR evropsku OR evropsko OR европа OR европи OR европу OR европска OR европској OR европску OR европско) (from:avucic OR from:adv_djukanovic OR from:SerbianPM OR from:TomaMomirovic OR from:Nevena_Djuric93 OR from:AcaSapic OR from:ZoranT11 OR from:Vladimir_Orlic OR from:VucevicM OR from:markodjuric OR from:NesaStefanovic OR from:MarijanNSS OR from:Jakssa077 OR from:VjericaR OR from:AlekSeselj OR from:NemanjaSarovic)',
            '(evropa OR evropi OR evropu OR evropska OR evropskoj OR evropsku OR evropsko OR европа OR европи OR европу OR европска OR европској OR европску OR европско) (from:BoskoObradovic OR from:SPDveri OR from:NovaStranka OR from:ArisMovsesijan OR from:demokrate OR from:ZoranLutovac OR from:SutanovacDragan OR from:PartizanusV OR from:DostaJeBilo OR from:SasaRadulovich OR from:BiljicVojin OR from:hanaadrovic)',
            '(evropa OR evropi OR evropu OR evropska OR evropskoj OR evropsku OR evropsko OR европа OR европи OR европу OR европска OR европској OR европску OR европско) (from:SlobodaIPravda OR from:DraganDjilas OR from:BorkoStef OR from:MarinikaTepic OR from:DanijelaGruji2 OR from:ZdravkoPonos OR from:WhistlerDick OR from:niinochka OR from:anna_bubisha OR from:StrankaNarodna OR from:jeremic_vuk OR from:MiikiAleksic)',
        ],
    'ukrajina':
        [
            '(ukrajina OR ukrajini OR ukrajinu OR ukrajine OR donbas OR donbasu OR donbasa OR kijev OR kijevu OR kijeva OR украјина OR украјини OR украјину OR украјине OR донбас OR донбасу OR донбаса OR кијев OR кијеву OR кијева) (from:avucic OR from:adv_djukanovic OR from:SerbianPM OR from:TomaMomirovic OR from:Nevena_Djuric93 OR from:AcaSapic OR from:ZoranT11 OR from:Vladimir_Orlic OR from:VucevicM OR from:markodjuric OR from:NesaStefanovic OR from:MarijanNSS)',
            '(ukrajina OR ukrajini OR ukrajinu OR ukrajine OR donbas OR donbasu OR donbasa OR kijev OR kijevu OR kijeva OR украјина OR украјини OR украјину OR украјине OR донбас OR донбасу OR донбаса OR кијев OR кијеву OR кијева) (from:BoskoObradovic OR from:SPDveri OR from:NovaStranka OR from:ArisMovsesijan OR from:demokrate OR from:ZoranLutovac OR from:SutanovacDragan OR from:PartizanusV OR from:DostaJeBilo OR from:SasaRadulovich OR from:BiljicVojin OR from:hanaadrovic)',
            '(ukrajina OR ukrajini OR ukrajinu OR ukrajine OR donbas OR donbasu OR donbasa OR kijev OR kijevu OR kijeva OR украјина OR украјини OR украјину OR украјине OR донбас OR донбасу OR донбаса OR кијев OR кијеву OR кијева) (from:SlobodaIPravda OR from:DraganDjilas OR from:BorkoStef OR from:MarinikaTepic OR from:DanijelaGruji2 OR from:ZdravkoPonos OR from:WhistlerDick OR from:niinochka OR from:anna_bubisha OR from:StrankaNarodna OR from:jeremic_vuk OR from:MiikiAleksic)',
            '(ukrajina OR ukrajini OR ukrajinu OR ukrajine OR donbas OR donbasu OR donbasa OR kijev OR kijevu OR kijeva OR украјина OR украјини OR украјину OR украјине OR донбас OR донбасу OR донбаса OR кијев OR кијеву OR кијева) (from:Jakssa077 OR from:VjericaR OR from:AlekSeselj OR from:NemanjaSarovic)',
        ],
    'putin':
        [
            '(putin OR putinu OR putina OR путин OR путину OR путина) (from:avucic OR from:adv_djukanovic OR from:SerbianPM OR from:TomaMomirovic OR from:Nevena_Djuric93 OR from:AcaSapic OR from:ZoranT11 OR from:Vladimir_Orlic OR from:VucevicM OR from:markodjuric OR from:NesaStefanovic OR from:MarijanNSS OR from:Jakssa077 OR from:VjericaR OR from:AlekSeselj OR from:NemanjaSarovic)',
            '(putin OR putinu OR putina OR путин OR путину OR путина) (from:BoskoObradovic OR from:SPDveri OR from:NovaStranka OR from:ArisMovsesijan OR from:demokrate OR from:ZoranLutovac OR from:SutanovacDragan OR from:PartizanusV OR from:DostaJeBilo OR from:SasaRadulovich OR from:BiljicVojin OR from:hanaadrovic)',
            '(putin OR putinu OR putina OR путин OR путину OR путина) (from:SlobodaIPravda OR from:DraganDjilas OR from:BorkoStef OR from:MarinikaTepic OR from:DanijelaGruji2 OR from:ZdravkoPonos OR from:WhistlerDick OR from:niinochka OR from:anna_bubisha OR from:StrankaNarodna OR from:jeremic_vuk OR from:MiikiAleksic)',
        ],
    'rusija':
        [
            '(rusija OR rusiji OR rusiju OR rusije OR ruska OR ruski OR rusko OR русија OR русији OR руска OR русију OR русије OR руски OR руска OR руско OR moskva OR москва OR moskvi OR москви) (from:avucic OR from:adv_djukanovic OR from:SerbianPM OR from:TomaMomirovic OR from:Nevena_Djuric93 OR from:AcaSapic OR from:ZoranT11 OR from:Vladimir_Orlic OR from:VucevicM OR from:markodjuric OR from:NesaStefanovic OR from:MarijanNSS OR from:Jakssa077 OR from:VjericaR)',
            '(rusija OR rusiji OR rusiju OR rusije OR ruska OR ruski OR rusko OR русија OR русији OR руска OR русију OR русије OR руски OR руска OR руско OR moskva OR москва OR moskvi OR москви) (from:BoskoObradovic OR from:SPDveri OR from:NovaStranka OR from:ArisMovsesijan OR from:demokrate OR from:ZoranLutovac OR from:SutanovacDragan OR from:PartizanusV OR from:DostaJeBilo OR from:SasaRadulovich OR from:BiljicVojin OR from:hanaadrovic OR from:NemanjaSarovic)',
            '(rusija OR rusiji OR rusiju OR rusije OR ruska OR ruski OR rusko OR русија OR русији OR руска OR русију OR русије OR руски OR руска OR руско OR moskva OR москва OR moskvi OR москви) (from:SlobodaIPravda OR from:DraganDjilas OR from:BorkoStef OR from:MarinikaTepic OR from:DanijelaGruji2 OR from:ZdravkoPonos OR from:WhistlerDick OR from:niinochka OR from:anna_bubisha OR from:StrankaNarodna OR from:jeremic_vuk OR from:MiikiAleksic OR from:AlekSeselj)',
        ],
    'nato':
        [
            '(nato OR нато OR potus) (from:avucic OR from:adv_djukanovic OR from:SerbianPM OR from:TomaMomirovic OR from:Nevena_Djuric93 OR from:AcaSapic OR from:ZoranT11 OR from:Vladimir_Orlic OR from:VucevicM OR from:markodjuric OR from:NesaStefanovic OR from:MarijanNSS OR from:Jakssa077 OR from:VjericaR OR from:AlekSeselj OR from:NemanjaSarovic OR from:PartizanusV OR from:DostaJeBilo OR from:SasaRadulovich OR from:hanaadrovic OR from:ZoranLutovac OR from:SutanovacDragan)',
            '(nato OR нато OR potus) (from:SlobodaIPravda OR from:DraganDjilas OR from:BorkoStef OR from:MarinikaTepic OR from:DanijelaGruji2 OR from:ZdravkoPonos OR from:WhistlerDick OR from:niinochka OR from:anna_bubisha OR from:StrankaNarodna OR from:jeremic_vuk OR from:MiikiAleksic from:BoskoObradovic OR from:SPDveri OR from:NovaStranka OR from:ArisMovsesijan OR from:demokrate OR from:BiljicVojin)',
        ],
    'amerika':
        [
            '(amerika OR američke OR SAD OR americi OR ameriku OR američka OR америка OR америчке OR америци OR америку OR potus OR америчку OR америчка OR američki OR амерички) (from:avucic OR from:adv_djukanovic OR from:SerbianPM OR from:TomaMomirovic OR from:Nevena_Djuric93 OR from:AcaSapic OR from:ZoranT11 OR from:Vladimir_Orlic OR from:VucevicM OR from:markodjuric OR from:NesaStefanovic OR from:MarijanNSS OR from:Jakssa077 OR from:VjericaR)',
            '(amerika OR američke OR SAD OR americi OR ameriku OR američka OR америка OR америчке OR америци OR америку OR potus OR америчку OR америчка OR američki OR амерички) (from:BoskoObradovic OR from:SPDveri OR from:NovaStranka OR from:ArisMovsesijan OR from:demokrate OR from:ZoranLutovac OR from:SutanovacDragan OR from:PartizanusV OR from:DostaJeBilo OR from:SasaRadulovich OR from:BiljicVojin OR from:hanaadrovic OR from:NemanjaSarovic)',
            '(amerika OR američke OR SAD OR americi OR ameriku OR američka OR америка OR америчке OR америци OR америку OR potus OR америчку OR америчка OR američki OR амерички) (from:SlobodaIPravda OR from:DraganDjilas OR from:BorkoStef OR from:MarinikaTepic OR from:DanijelaGruji2 OR from:ZdravkoPonos OR from:WhistlerDick OR from:niinochka OR from:anna_bubisha OR from:StrankaNarodna OR from:jeremic_vuk OR from:MiikiAleksic OR from:AlekSeselj)',
        ]
}
