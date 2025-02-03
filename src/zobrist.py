import chess

random_array = [14390040796412792165, 14719554940303223030, 15377179358137496429, 5904743379265530689, 14315091928874902668, 2669977067888677968, 1239590814252474619, 8281486885890932464, 5238511851288986987, 15284590377083636679, 13625248982751825372, 8933921912240983972, 16358804410351275977, 8053301540991480580, 17844231859910991510, 1241186931323825475, 9986609022931783274, 3552229677779845835, 5914128521990066611, 8700952984770776138, 5983393397243276828, 4440122122157746956, 2566230515486331994, 3367370104443991828, 5406113622042787674, 13276885272977636996, 12883210177572761134, 3260289031806247045, 10913179132839050461, 13045041399183833478, 17234301849116902207, 9025022596321692101, 7677569885823738818, 9727192481311439168, 1703467717056301647, 7511486967047593013, 10756904796070186898, 16454357552368909408, 600043873689617873, 11854581155478427612, 4229095437360535314, 14080942721280595628, 5793742713955798910, 12629876778968078536, 7257647505314899872, 16248241574883117802, 2341789995837129488, 3929847201927896914, 18396885927339119626, 9824877835258944289, 13470868793161653671, 1704137810769941738, 1558008956662587470, 7626514952876502465, 9840309097865594968, 17710155818873554501, 8610251145677476826, 6832547159699030149, 185683295305309835, 9719547224082669231, 667066352220275051, 8230373217479972188, 2546399100437148758, 1236727438194834157, 11241659225479233737, 10993754608088404185, 14103745144592259403, 2875401728403635809, 17179500402872727294, 15143285167327349930, 1375454819278984115, 10810583566601094497, 5848156596560784600, 13445406971992697982, 3155885287340920362, 8560070239209093206, 13330050281669328888, 13048890476178885696, 446732665532162186, 11547941722884551992, 17723284751546823637, 12788245634583442191, 6038041359045152240, 8717168900704214927, 11185616652745253476, 4582850841790952904, 15328474142578339009, 16785507188036095731, 7624630326847049263, 1893056466959100252, 5914254632105435159, 11624952288331212640, 17387218501462415230, 4355454336185596296, 7135839202574987028, 6061894122895201344, 14591915183572730664, 1336977573352624025, 11691983222119989771, 7562159405846549231, 5441821427725372590, 6594911927976108959, 3654549367361371899, 14794241241667120073, 6320624652151111835, 9040908396625270722, 6340996839112943913, 15610051431256579363, 11670293986880315265, 17667261033078307638, 18123349580382260016, 2681187430761397845, 17415790391021815641, 4111217273085860241, 15640727139077702548, 10634412415844018579, 5745733590271778533, 12537822802172335352, 10496069186895586125, 68289191098206874, 14103208748499555026, 11577917131441242719, 10533280172743487180, 5486709905199910457, 4204191826137010977, 4117341652102389502, 8499364974983969511, 12255740747549141083, 305492811096537367, 16484508425160940247, 12495663868141123890, 15934261629091089764, 7825700930318734170, 7155570621447162559, 12158104252450950373, 15514158532498118251, 14965468997281687622, 8808453343809064148, 15830195260256448361, 8524207981511638999, 9089628089812853533, 5740071649438776993, 1343993488427518185, 10031366424765268995, 8822732721743013131, 14975622931613723185, 3510718426213104040, 16718258648387266397, 7881738605839725294, 8335020841301943464, 10443114002452566129, 5470146680997358171, 12311874392282122937, 16527563735990789094, 4003698821812135556, 15388686859659230865, 4563691721516376519, 8939067834030264646, 1725586831892467697, 1516778775585785492, 15494288929546793563, 10802569803946696437, 471731395022571518, 13420708580407961734, 18273552617231221333, 8372162020801967247, 7976038235448687512, 397132343947946366, 7803937197203521378, 4851811709668195011, 6376750298301678667, 12633685553085755724, 13197268338708725386, 12380936632028139160, 8584062847708982201, 4792707070196415252, 12921352197312211279, 5757746564586250531, 15358383784657640457, 2375430309224557188, 899076688254557893, 7041490909608895823, 15201527772307522390, 6079003469783750422, 13162447485279749138, 18253934167862605635, 7917431272813848891, 10494802479003950033, 11281498781682882056, 6290087626571179681, 5431178121975665437, 12859773859272072718, 12675363463290871716, 1321052868111869352, 3503646231657450969, 12600924803263913276, 2737586073397194296, 14717976498636793465, 14646084849796844933, 11118368639074959807, 1007425903584053992, 16214979746265050931, 16688983016830317576, 17402976449945367065, 4918582890707376962, 16024426333024626903, 17434597806098934999, 6430408935333824892, 7832060084053710538, 11158386205444210876, 10923479253893419410, 11840669782641458115, 15888748387107461814, 4032050791990163113, 7410204472175940833, 13684404274904294523, 16358625907807595272, 4392695586522897173, 13300949717019489913, 16395743677909226378, 1089653022200067762, 3069387608013518119, 14648775073603226777, 5310131529991273745, 7017437620702192851, 16614033811738056597, 1861208206965521914, 2165273397810925612, 982161526185949391, 221666793067507460, 17067445188005149211, 4409636029491869404, 7662957521080478240, 4349255421185109638, 8020188160651096142, 4696451519367058054, 6993701340369633876, 15206095967495836438, 3552493007364515163, 2257742258155213514, 103784247544701218, 9253819470391115876, 15042275259013375409, 8683039544059920105, 13014369279988558378, 12862960353576813780, 11361875454311858802, 14509893737913142114, 17662132341620827676, 2945207564682302734, 6514626858281809285, 15799297008629702650, 13420494465170781190, 7523287819117012277, 17083786788792213913, 4024208165292199114, 1203000929150332018, 16446675229854624620, 10076164260858557047, 8562836888833010738, 2338785456491814269, 6802521151252871106, 10665954921954874410, 2016775067414267713, 9552487870649962622, 5601360917174632538, 10208734697021674095, 7429371667918435532, 12892119435128268657, 11895076823467584174, 7924501629705307694, 2902485537162211093, 3687304247784848110, 17965708971157737740, 1305666722744904437, 15758635854768017072, 3365322706024577249, 4524371708565509398, 13681725277102676016, 12155306221732981313, 5928290914226245130, 16037688043700250432, 16481266583192590895, 16224121388030376622, 15763432266808041461, 981781310494933890, 16206409860241893798, 119583216221173933, 17509503318074292103, 18091944289318489933, 15026525772087826637, 9225830280032681599, 9492171642566525874, 3212286613603639102, 1755764205505696162, 2175614187805674394, 3396144161682519254, 14055031853823511463, 6872991847729057805, 9288890192067377082, 4881450343447365066, 12452882756883014750, 16331663014012429270, 8867191049493542636, 16738195522134189782, 7972256517385894124, 11530928754542723544, 8804098745132541179, 726293498762641672, 3704547085345920132, 6861113524419687507, 12077842441044699247, 15401966903479799125, 2817638019731641783, 13120012738941329985, 4215179587072355463, 15581697247390868128, 1714874980578098804, 10163311544041065293, 8667072582560171236, 7646794376494414980, 15841241401483875215, 11148338183407889397, 18312700096209443149, 4234118974981450140, 13201244577854926926, 11016611375705308114, 14047135407111049364, 16608250632593464948, 7954421203666400418, 16002360600151984930, 16010770430339897921, 15954221085379907971, 8954095659636014466, 10254454195350675013, 8715745713112412274, 2347506761752091513, 14066339809553282146, 3733413373185719415, 5190186886661240041, 8855968077857467950, 4884099029838313556, 9708220581802107705, 7852099631679950763, 6339964567948886349, 13292583259089832477, 14559914835068251908, 7316902693952699550, 8146899706159214771, 10589551983972374538, 2208609339956291304, 4588309144159685019, 5588158174818023809, 15562343316405170952, 14271758446007271322, 5099667663873290897, 10794045616132643271, 14104983615907331348, 3846944187528311764, 890522483399832963, 10831327382561311175, 12107950974623744287, 13609275842980865911, 13228131836027914399, 9381495327688403576, 6461606515415828317, 6642806780977995283, 11471710378689305807, 18241198669255860931, 4582048547545334935, 4028061146711806185, 4815307549771923745, 10142034388424251722, 9251821560753984859, 8203282920775583949, 16133609097802088168, 13667963724247599057, 5350786083366725914, 16035568934393045959, 4682001817469719321, 387109666996865696, 3853115282436268671, 4496900584319703938, 9343736496980043071, 2948086468231918810, 5442757837627570462, 11458307618225006522, 16352115040187572157, 17585121042254181848, 6179531111436386071, 7800863519229609161, 2481733171488824699, 15818026457083911272, 17449106266805795851, 4287970335661110794, 12171482745313579012, 9907893317226647697, 14681198634415216596, 9854802822127393494, 18045249707774017847, 1647434675568268965, 8408086641089468208, 6050374051870356629, 7530200823621583819, 12406449197242208054, 8362789812128451543, 11530327564313651669, 5367204919356627059, 12508643703753845940, 14308288650590202887, 13854446840144546789, 6652396163813998962, 9551022535164739877, 6217441534920403199, 12661468310772571065, 17403756502413674445, 8291239422548854810, 387468725030357838, 12257614576379239597, 16788704031800527940, 234313535253029654, 17172245456647898485, 11427739924236342581, 14433335552806569701, 6198078532659622294, 13558861156904850003, 11548271939185036049, 846942278253853975, 11234365042878876791, 5988904603540920877, 14739762188906777572, 15463937701265658984, 3988093718772818487, 11390907436916601295, 7299928735651865271, 10381865947585068167, 9361654565255246336, 3484512441530186131, 17050722829979766553, 6284561434504538773, 4399141908839407395, 2441740904326443437, 8370767076228603468, 13519551898192952201, 18415456677301068540, 13611035580987939378, 17714245585524514933, 380690433937338511, 16001665761258604761, 4832797667180035650, 15494410931609791190, 18025200201296724368, 6371144303588630866, 4555383199175479493, 1300656554831714548, 5679783646655447575, 6913127643418578466, 14811217545421369826, 10533945568617171726, 14543777642774625520, 15969247255688115427, 358467489435925590, 16561422285774703761, 6676264152036669671, 991749076513909812, 12641629717792564683, 2507535798358228369, 11011166076532515314, 3388902719565279979, 10499597613085764931, 10955875944542046112, 11009378934944619315, 15426855282383501254, 9935140201127301473, 7006404622031149749, 10588683065700472819, 8440518330982509886, 13900706776705545961, 17630099500629763183, 9707930364591555955, 3787623827374037327, 2412522130269383419, 1239264794425257373, 3660062323642068337, 345670891565583029, 12680666188916747325, 14283209016281455824, 1207562819461445011, 17262469894499158836, 9756966082391381523, 13230763941419883806, 4230204261908728297, 12572246330488840624, 7624823514843315542, 1706233183991630641, 3464243911201284190, 12780214934336356215, 10164309859911247851, 2979676666712967635, 3264487915616310498, 9380507334719883797, 16871895890435651378, 2385941087886652352, 4252614009293338192, 8527796698562561535, 5567268600246284361, 13170829173475850492, 5707974259912903695, 17050196229328510125, 6783341196544277226, 6561247871793718759, 14568494083480136914, 17522329571236028751, 7101515975562237607, 192730432245044177, 8050644727448583038, 15050832767553695076, 924690111028388810, 5337635015538029498, 3714439004266612556, 17131532686428373307, 4779947677260564087, 3728689853785227948, 9688444149755175222, 4119786419521755526, 6047774964979330716, 12899296384153996592, 3219075652812818258, 954003436864337124, 522079519945017328, 11204584348161929452, 11660576944034537778, 11529344838621622196, 397327018179726475, 7565309499282720603, 17126372379562127848, 4256460438794733183, 6387730090979830680, 15311594530745909911, 8332412421609610683, 786117461041842907, 5427479762587685720, 3066759773557681777, 5771936075113599543, 12575149411350389533, 18376915085968646790, 5459109122949351395, 11846957927181810783, 853195433381076987, 9448286443256274102, 12118138723615724832, 12187701154736736645, 12128582211274897603, 17749320790272740883, 2740381139836980992, 18021739059515767679, 17819626499645387722, 763957367404092515, 16077658411917208652, 11981341829566966254, 13507041331048182163, 7258738139815747115, 12818957995765804588, 16055666457869858713, 13508490820195151025, 18360569998861376217, 425603038678170275, 8906546136237555673, 296820204935253379, 18323695689388957812, 10981539286189706916, 1003587955373884229, 15381906276740204685, 12886302150312066704, 14445400928772792058, 10931351564458592522, 16633190201002798368, 2047698739013374587, 5460733852055478633, 7786124318869844219, 16156629964904758382, 8809013292874635999, 13376022404635769550, 16852170513936453447, 11990377515394289629, 15261617469713096408, 12769472171896578072, 2875943014182617726, 9334515967383484650, 4531277950369785683, 3692304975976417165, 11051531930097534612, 10367475900581483783, 71974902139291537, 12306899943782251708, 14228218006819104907, 10374583234730625906, 8881697736090020275, 10040981967469725892, 3383561260909831816, 12670841965948626965, 12346609723220870511, 9661222969179410662, 9913924149992592978, 14259712841642863625, 17502998435741343636, 9118602801645272594, 2656881878146129952, 12139910125404936312, 10712947008284004801, 8134636954748226633, 18107370661379394594, 17262567459957003309, 7583640355005416468, 8146288995594189470, 16267644481585087726, 12968306727491560078, 15931168575422449871, 7891400016829741144, 14347112077577388903, 7670799677335151309, 13228279924085228323, 7504828720302381921, 18156005522735226731, 17321350090029285476, 13506060181031602609, 14478831645420247956, 15320951798506883386, 429719783009399022, 15382014731410826073, 3495292294343605022, 1501985484085789008, 11909660113207998511, 6149845075931140781, 5040685712820092111, 13449706465697524254, 12203164354583291934, 13104127687013107029, 11961574144959205144, 3420514316816209740, 8222310157325808797, 16665742137487244436, 16497590118631004599, 11252276525393949466, 15381307967899425996, 3971300990132703945, 6361144454622201295, 13723340606538393594, 10295777766730017572, 17036325932522700677, 9469566329255852559, 3984668063214597791, 6814489478251603435, 5960134525347134477, 11050093028147099255, 10524487296109944634, 6604593363549492638, 212999212069924278, 15442391621167299416, 14475053907932939581, 15591562850368722524, 17254146485797883566, 37932236411825945, 186646610047459322, 7103530253366939182, 4932146749457282596, 3204352985154942913, 15833685802591002628, 10343611983092564435, 338076051067819162, 16561491253920818068, 18440682970690432018, 6512986022099632467, 3113286870463663845, 10195752007754591662, 10432610700560100640, 4220573765696734352, 4368059495448570903, 570285652980133844, 2732836243333970775, 2290102217800546, 9595712307223755035, 628115078355916384, 15297563812563087259, 5329837981574693767, 12524556299673279505, 3693977712226303380, 1355243263094119116, 6658542664185933584, 3315112644996739945, 7198447052344299731, 371850231425960309, 6545784867294756999, 15405995618326770350, 8166598326081682851, 7241638979260720038, 5337760695632887600, 11139275690979935608, 17791680212816615547, 8623052595367797616, 1050431364922259519, 12431068014305137883, 6592368609051304522, 3493672596410300233, 1266615694858233458, 4875944892580331358, 4669496277580464324, 2991666679028855512, 13399859968397132784, 8609585612394983014, 10286503785722054530, 2886258334681221303, 13925345038552404549, 564697953560252948, 4189279582463597977, 8865621997972225668, 1147008022913611809, 6090645533392958143, 5248858418321701836, 591108676306410287, 1990276325359884885, 1376062945222121702, 644204902970206623, 168196329510931171, 9065007789326820946, 15846456184735769107, 3279602366778389893, 12672228295623493630, 4211150131894268406, 9831178252946144338, 5557823246948368263, 3711265473668720977, 10675147758251787749, 7757623729564918009, 6048361682574821357, 14413324167234163988, 2005227533939746733, 892601112015653159, 6040462137551171547, 9560262447267514295, 10208755765076907032, 10612654434415796716, 13252050970966969152, 13203473181411395022, 1527494075366450099, 16474675976823479135, 5173849023361806027, 9330231573660941595, 13660192463007915301, 4750907946423158626, 2995002171726246281, 12367475074729486949, 4344545106417422500, 5469932719312114496, 5207455862455172513, 12494082996984726924, 3740428520387184825, 16771517202932390112, 17089087194689113139, 3813992253719329063, 13657592591657301253, 10121774295962980512, 13624325660798665183, 13691822722099642343, 4602872020064318255, 732389740482986776, 15616510334986581733, 10782892655681131233, 4458089365020313341, 15607236301254847124, 7807015606727758828, 13759992889878146623, 1896492762878664064, 11869099080245448617, 13991184197839766495, 13040382414943100947, 6336228908254231163, 780183554398616665, 447964257326750676, 13441264463045737714, 289009762642177173]


class ZobristHash():

    def __init__(self):
        self.array = random_array

    def hash_board(self, board):

        zobrist_hash = 0

        # piece positions
        for square in range(64):
            piece = board.piece_at(square)
            
            if piece is not None:
                piece_index = (piece.piece_type - 1)*2 + int(piece.color)
                zobrist_hash ^= self.array[64*piece_index + square]

        # castling
        if board.has_kingside_castling_rights(chess.WHITE):
            zobrist_hash ^= self.array[768]
        if board.has_queenside_castling_rights(chess.WHITE):
            zobrist_hash ^= self.array[768+1]
        if board.has_kingside_castling_rights(chess.BLACK):
            zobrist_hash ^= self.array[768+2]
        if board.has_queenside_castling_rights(chess.BLACK):
            zobrist_hash ^= self.array[768+3]

        # en-passant
        if board.ep_square:
            # But only if there's actually a pawn ready to capture it. Legality
            # of the potential capture is irrelevant.
            if board.turn == chess.WHITE:
                ep_mask = chess.shift_down(chess.BB_SQUARES[board.ep_square])
            else:
                ep_mask = chess.shift_up(chess.BB_SQUARES[board.ep_square])
            ep_mask = chess.shift_left(ep_mask) | chess.shift_right(ep_mask)

            if ep_mask & board.pawns & board.occupied_co[board.turn]:
                zobrist_hash^= self.array[772 + chess.square_file(board.ep_square)]

        # turn
        if board.turn == chess.WHITE:
            zobrist_hash ^= self.array[780]

        return zobrist_hash