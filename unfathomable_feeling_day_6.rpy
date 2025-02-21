
label unfathomable_feeling_day_6:
    window hide

    $ renpy.pause(1.0, hard=True)

    $ backdrop = "days"
    $ new_chapter(6, u"Непостижимое чувство.\nШестой день")
    $ persistent.sprite_time = "day"
    $ day_time()

    $ renpy.pause(1.0, hard=True)

    scene int_house_male_day with fade

    play music music_list["i_want_to_play"] loop fadein 2
    play ambience ambience_lake_shore_day loop fadein 4

    window show

    "Я проснулся на удивление спокойно. Мне никто не щекотал нос, моя спина не была мокрой из-за росы, и я не сидел в накалённом дотла автобусе. За окном щебетали ранние пташки, и как всегда был природный порядок."
    
    scene ext_house_male_day with dissolve

    play ambience ambience_camp_center_day loop fadein 4

    "Подтянувшись и зевнув, я вышел на улицу."

    window hide
    scene ext_houses_day with dissolve

    $ renpy.pause(1.0, hard=True)

    scene ext_washstand_day with dissolve

    $ renpy.pause(1.0, hard=True)

    scene ext_washstand2_day with dissolve
    window show

    "Я просто аккуратно пошёл к умывальникам, ещё раз подтянувшись. Вода сегодня не была ледяной, она была холодной, с нотками теплоты в вырывающейся из смесителя струе. "
    
    scene ext_washstand_day with dissolve

    "Нет, сегодняшнее утро однозначно хотело меня удивить и у него получилось. На улице стояла тихая погода, не нарушаемая даже дыханием ветра, солнце неторопливо отдалялось от горизонта, озаряя небо лазурным сиянием." 
    "Не знаю отчего, но сейчас очень захотелось пойти на пристань."

    scene ext_boathouse_day with fade 

    play ambience ambience_boat_station_day loop fadein 4

    "Пройдя по каменным плиткам и свернув налево по тропинке я оказался на месте. Я не ошибся. Зрелище действительно было завораживающим. "
    "Светило, ещё не успевшее покинуть пределы горизонта, освещало весь лагерь в яркие янтарные тона, словно ты смотришь на мир через призму модных очков оранжевого цвета. "

    show un normal pioneer far with dissolve

    "О воде говорить не приходилось — она вся извивалась в тёплых бликах солнца. Спустив свой глаз ещё ниже, я увидел силуэт, сидящий на крайней доске пирса, с которой я разок удачно навернулся. "

    show un normal pioneer with dissolve

    "Старые воспоминания уже было снова начали терзать меня, но я, отбросив ненужные мысли подошёл к девушке с двумя хвостиками, которые немного свисали вниз."
    
    me "Привет, Лен!"
    "Поприветствовал я девушку, вдохнув полной грудью аромат утра. Рядом с леском, где удачно расположилась пристань, пахло хвоей."
    
    un "Привет."
    "На мгновение мне показалось, что счётчики смущения Лены сдали обороты, и потому сейчас частично неисправны."
    
    me "Прекрасная погода, не так ли?"
    "Я тепло улыбнулся ей, всё же стоило подружиться со всеми обитателями этого лагеря."
    
    "Обитателями? Старое слово прижилось, но сейчас самое время подыскать ему замену."
    
    show un smile pioneer with dspr

    un "Как же ты прав!"
    "Улыбнулась девушка без единой капли смущения на лице."
    
    show un normal pioneer with dspr

    "Ветер, словно подслушав наш разговор, решил доказать, что не всё так хорошо, как кажется. Холодный поток воздуха пробил до костей, и даже тёпленькое солнце сейчас не могло отогреть нас." 

    show un shy pioneer close with dspr

    "Лена машинально поёжилась, и прислонилась ко мне. Она так близко... Я чувствую её дыхание, её тепло."
    
    "Она поворачивается ко мне и смотрит прямо в глаза. {w}Как я раньше не замечал её прекрасные изумрудные глаза? Такой пронзительный взгляд и аккуратный кристалл зрачка."
    "Это было пыткой. Она приближалась своими губами к моим, и я уже чувствовал тепло её дыхания."
    
    "\"Стоп-кран! Активировать рычаги! Надо спасать ситуацию. Загрузить лучшие воспоминания с Мику, отдать прямой контроль над телом! Бегом, шевелитесь!\"{w} – именно так бы мозжечок отдавал сигналы нейронам, которые затуманились благодаря этой пионерке."
    
    "Я отпрянул от Лены и встал, отряхнувшись."

    show un sad pioneer with dspr
      
    me "Прости Лена. Так нельзя. Ты сама всё понимаешь."

    "Я выговорил это, стараясь снова ненароком не взглянуть ей в глаза, тогда меня уже ничего не спасёт."
    
    scene ext_pathway_boat_station with dissolve

    $ unfathomable_feeling_open_image_gallery("bg", 2, 4)
    
    "Спустя мгновение я развернулся и быстрым шагом пошёл по тропинке обратно в лагерь. Взгляд на спине пытался прожечь меня насквозь, чтобы хоть как-нибудь остановить."

    scene ext_houses_day with fade 

    play ambience ambience_camp_center_day loop fadein 4

    "Я решил сразу зайти в столовую, пока есть места и перекусить чего-нибудь."
    
    play sound sfx_stomach_growl

    "Мой желудок заурчал, совершая акт согласия с произнесённым, и я уверенным шагом пошёл в сторону цели."

    scene int_dining_room_day
    show ck normal 
    with fade

    $ unfathomable_feeling_open_image_gallery("bg", 3, 1)

    play music music_list["reflection_on_water"] loop fadein 2
    play ambience ambience_dining_hall_empty loop fadein 4

    "В столовой оказалось несколько пионеров и заспанная повариха. Я подошёл к ней. Интересно, что они могли успеть приготовить в такую рань?"
    
    show ck sad with dspr

    "Повар одарила меня недобрым взглядом, а также булочкой с какао."

    scene int_dining_table_day with dissolve

    $ unfathomable_feeling_open_image_gallery("bg", 3, 2)

    "Я сел за свободный столик и принялся уплетать еду. К моему удивлению, булочка оказалось с повидлом, а какао — нормальный, с молоком, а не разбавленный, как всегда." 
    "Надо почаще сюда с утра заходить. Всю следующую неделю готов рано вставать, ради такого пиршества-то. {w}Правда, содержимое подноса быстро усвоилось в недрах моего организма и я поспешил к выходу."

    scene ext_dining_hall_near_day with dissolve

    play ambience ambience_camp_center_day loop fadein 4

    "Сейчас примерно 7 утра, куда можно пойти? Мику скорее всего, как и остальные девочки, спит, а к кибернетикам без интереса как-то. В библиотеку! Правда, скорее всего она закрыта, но попытка, как говорится, не пытка!"
    
    scene ext_library_day with fade

    "Библиотека была отперта, и я, совершив нехитрые махинации с дверной ручкой, оказался внутри."
    
    scene int_library_day with dissolve

    play music music_list["silhouette_in_sunset"] loop fadein 2
    play ambience ambience_int_cabin_day loop fadein 4
    
    "В помещении, у правой стенки, на диване находилась Женя и, откровенно говоря, спала. Бедняжка, даже до выхода не доковыляла."
    
    "Решив не будить девочку я прошёл вдоль одной из полок, перебирая пальцами корешки переплётов. Мой палец наткнулся на выпирающую обложку сборника произведений Гоголя." 
    "С самой нашей первой встречи я спросил у Жени про зарубежную фантастику, но ответом мне было лишь холодное \"Нет\"."
    "Я открыл содержание на последней странице и пробежался по нему взглядом «Ревизор», «Ночь перед Рождеством», повесть о капитане «Копейкине»."
    "Ага, вот они, – «Мертвые души». Повесть занимала львиную часть книги, и я сел на свободный стул в углу, после чего принялся читать, вспоминая о школьных временах и изредка поддаваясь ностальгии."

    $ unfathomable_feeling_timeskip()

    play sound sfx_dinner_horn_processed

    "Время пролетело незаметно: спустя несколько десятков страниц раздался сигнал на завтрак. Я аккуратно зашёл за полку, дабы не привлечь лишнего внимания и, подождав пока Женя выйдет, покинул помещение следом. "
    "Выждав время, пока девушка уйдёт на значительное расстояние, я нырнул на соседнюю тропинку, и «как бы невзначай» столкнулся с ней. Она не поздоровалась со мной, да и вообще, её лицо не выражало ни единой эмоции. Я лишь ускорил шаг."
    
    scene ext_houses_day with dissolve

    play music music_list["confession_oboe"] loop fadein 2

    "Солнце уже отлепилось от горизонта, и прекрасный пейзаж янтарных облаков был утрачен. Его место занял голубой, с отливами розового небосвод с редкими облаками. Ветер снова притих, будто готовясь с силами для решающего удара."
    
    scene int_dining_hall_people_day with fade

    play ambience ambience_dining_hall_full loop fadein 4

    "Столовая, по своему определению была битком, и попытки найти хоть какое-то местечко для уплетания геркулесовой каши было проблематично. "
    "Свободных столиков не нашлось, а есть стоя – не вариант. Поэтому, с ноткой досады, я отдал поднос обратно повару, а сам взял пару булочек с раздачи. Решив расправится с ними по дороге, я вышел из столовой." 
    
    scene ext_dining_hall_away_day with dissolve

    play ambience ambience_camp_center_day loop fadein 4

    "Птички уже готовились начать утреннюю серенаду, где-то даже слышался одинокий соловей. Я же шёл по прохладному асфальту, смотря себе под ноги и заедая одиночество очередной булкой."

    $ renpy.pause(1.0, hard=True)

    "Когда я прошёл ещё пару метров, из-за угла вышло длинноволосое чудо."
    
    show mi smile pioneer with dissolve

    mi "Привет, Семён!"
    "Она мило улыбнулась."
    mi "Ты уже поел?"
    "Она смотрела на булочки в моей руке."
    
    me "Да, поел."
    "Я улыбнулся ей в ответ."
    me "Правда столовая сейчас забита, я тебе булочек принёс."
    "Произнёс я, поднося пакет с булочками девушке."

    "Наш курс сильно поменялся и мы повернули в сторону домиков."

    scene ext_houses_day
    show mi normal pioneer
    with dissolve
    
    mi "Сейчас зайдём в кружок?"
    "Спросила Мику, заранее зная ответ."
    
    me "Ну пойдём, а тебе там не надоело самой-то?"
    
    mi "Вообще, уже начинает раздражать."
    "Сказала девушка, когда с очередной булочкой было покончено."

    scene ext_house_male_day
    show mi normal pioneer
    with dissolve

    mi "Но мы туда только гитару занесём."
    "Она резко развернулась и зашла в мой домик."

    hide mi with dissolve

    "Вот чем я точно не мог похвастаться — так это порядком. Даже в лагере я умудрился засрать свою комнату. Кровать была полностью расправлена, а какие-то свёртки валялись по полу."
    
    mi "Уютно у тебя тут."
    "Донеслось из домика."
    
    me "Я старался."
    "Я подмигнул девушке."
    
    show mi normal pioneer with dissolve

    mi "Ладно, пойдем уже."
    "Мику передала мне гитару и мы вышли, взяв курс на клуб."

    scene ext_houses_day
    show mi normal pioneer 
    with fade

    me "Какие планы на сегодня?"
    "Я спросил, так как понятия не имел, что мы будем делать после того как пройдём в музыкальный кружок."
    
    mi "Вообще меня Алиса приглашала сегодня на прогулку. {w}Прощальную."
    "Вздохнула Мику."
    
    me "Почему прощальную?"
    "Я прекрасно понимал о чём она говорит, но молился, чтобы это оказалось ложью."
    
    mi "Так завтра же конец смены."
    "Я услышал это." 

    scene ext_houses_day_monochrome
    show mi monochrome
    with dissolve

    play music music_list["farewell_to_the_past_full"] loop fadein 2

    "Ползунки «Контрастность», «Насыщенность» и «Яркость» окружающего мира поползли влево... {w}Всё вокруг меня потемнело."
    
    me "Почему? Обычно смены длятся по три недели!"
    "Я пытался ухватиться хоть за какую-нибудь теорию."
    
    mi "Ты прав, Семён. Но ты опоздал на две недели..."

    scene ext_houses_day
    show mi normal pioneer 
    with dissolve

    "Каждое слово фантомной болью отзывалось у меня в голове. Я столько упустил. Эта сделка начала принимать очень невыгодные для меня обороты."
    
    scene ext_musclub_day
    show mi normal pioneer
    with fade

    me "Мику. Выслушай меня. Мы должны выбраться отсюда, понимаешь?"
    "Я сам не верил своим словам. Надежда вновь встретится с ней угасала на глазах."
    me "Ты не заметила, что с вчерашнего дня я так странно себя веду?"
    
    mi "Конечно заметила, это очевидно."
    "Девушка с испугом в глазах смотрела на меня."
    
    me "Потому что этот я — настоящий."
    "Я ткнул пальцем себе в грудь."
    
    scene ext_music_club_veranda_day with dissolve

    "Её аквамариновые глаза заблестели, и она отвела их, открывая дверь в клуб."

    play sound sfx_lock_open

    "Справиться с замком у неё никак не получалось. Руки сильно дрожали, и она не могла попасть в скважину. Я аккуратно толкнул дверь. Открыто."
    
    scene int_musclub_day
    show mi sad pioneer
    with dissolve

    play ambience ambience_music_club_day loop fadein 4

    "Мику зашла внутрь, полностью потерявшись в себе."
    
    me "Мику, ты не рада? Объясни почему ты плачешь?"
    
    "Она нырнула в подсобку заперев за собой дверь. Я пару раз ударил по ней, а потом обернулся спиной и упал на пол, скользя лопатками по дереву."

    hide mi with dissolve

    play music music_list["trapped_in_dreams"] loop fadein 2
    
    me "Что случилось?"
    "Я пытался быть спокойным, но у меня не получалось."
    
    mi "Она... тоже... приходила... ко мне..."
    "Она еле разговаривала."
    mi "Каждый вечер, до вчерашнего дня... А когда после шахты я побрела домой, она предложила мне сделку. Если я..."
    "Она прерывисто вздохнула и продолжила."
    mi "Если я отправлюсь к тебе, то я больше не увижу тебя вновь."

    "Всё точь-в-точь..."

    mi "А то, что нас двое в одном мире, значит что мы больше не встретимся, Ты понимаешь это? Ты — эгоист!"
    "Она ударила в дверь, отчего последняя дрогнула. Из подсобки вновь слышны всхлипы."

    me "Мику, открой."
    "Я ткнул локтем дверь и привстал. "
    
    show mi sad pioneer with dissolve
    
    "К моему удивлению дверь открылась, а передо мною стояла заплаканная Мику."

    "Даже в таком виде она была милой, хотя её глаза выражали пустоту и безразмерную грусть."
    
    show mi sad pioneer close with dissolve

    "Я поддался к ней и обнял. Она не пыталась сопротивляться, просто расслабленно укуталась в мои руки, а носик уткнула в плечо. Я продолжал слышать всхлипы."
    
    me "Я сделал это только ради тебя."
    "Она прижалась ко мне ещё крепче."
    me "Мы выберемся отсюда. Обещаю."
    "На секунду всё прекратилось."
    
    mi "Обещаешь?"
    "Она выглянула из-за моего плеча и пыталась стереть слёзы с уголков глаз."
    
    me "Конечно!"
    "Я тепло улыбнулся Мику и расстройство начало медленно сходить с её лица."

    show mi sad pioneer with dissolve

    me "Ты так мила когда плачешь..."

    show mi sad pioneer close with dissolve

    "Я вновь обнял её."
    me "Но обещай больше не плакать из-за меня, хорошо?"
    
    mi "Ты сам знаешь что я не могу гарантировать тебе этого... но... я постараюсь."
    
    hide mi with dissolve

    "После этого девушка нехотя отошла от меня, зашла в подсобку, а я взял гитару и присел на стул у стенки. Мику вышла уже в нормальном виде, без капли грусти на лице. Она даже улыбалась."
    
    show mi cry_smile pioneer with dissolve

    me "Всё хорошо?"
    "Мику утвердительно кивнула в ответ и в клуб зашла Алиса."
    
    show dv grin pioneer2 at left
    show mi normal pioneer
    with dissolve

    play music music_list["my_daily_life"] loop fadein 2

    dv "Привет, голубки, готовы?"
    "Алиса опять усмехнулась, но без надменности и насмешки."
    
    me "Всегда готов!"
    "Отчеканил я. Рыжая кивнула и перевела взгляд на Мику."
    
    mi "Да..."
    "Мику ответила тихо, почти шёпотом. Алиса сразу же обратила на это внимание."
    
    show dv normal pioneer2 with dspr

    dv "Всё нормально?"
    "Её задорный голос смягчился. Она недобро стрельнула глазами в мою сторону."
    
    show mi smile pioneer with dspr

    mi "А? Да, конечно."
    "Девушка взбодрилась и улыбнулась."
    
    dv "Ну ладно, пойдём."
    "С этими словами наша проводница вышла за дверь, мы не заставили себя долго ждать, и вскоре в полном составе были на улице."

    scene ext_houses_day with fade

    play ambience ambience_camp_center_day loop fadein 4

    "Наша компания просто бродила по просторам лагеря, иногда останавливаясь на важных местах. Всё это время Алиса что-то рассказывала из истории смены, когда я ещё не приехал."
    
    show mi smile pioneer at left
    show dv smile pioneer2 at right
    with fade


    dv "...а Ульянка ему с досады мяч в голову зарядила, помнишь?"
    
    show mi laugh pioneer 
    show dv laugh pioneer2
    with dspr

    mi "Конечно, дорого обошлись ему эти конфеты."
    "Обе девочки захихикали."
    
    show mi smile pioneer
    show dv grin pioneer2 
    with dspr

    dv "Семён, помнишь вечер первого дня?"
    "Алиса с улыбкой посмотрела на меня."

    "«Извини, я попал сюда из будущего посредством прохождения пространственно-временных порталов, а потом, плюнув на всё, ещё и переместился между мирами, и единственное чем сейчас забита моя голова — это размышления о выходе."
    "Но, так как я переместился сюда только разумом, то воспоминания у меня только со вчерашнего дня, поэтому, скорее всего нет, не помню» {w}– ответ звучал крайне неубедительно, и, скорее всего, после него я бы отправился исследовать отколупывающуюся штукатурку в здании с желтыми стенами."
    
    me "С трудом."
    
    dv "Как же, я же тебя на пляже чуть не утопила, потом вещи твои забрала!"
    "Усмехнулась девушка, что же, похоже на Двачевскую."
    
    show mi laugh pioneer 
    show dv laugh pioneer2
    with dspr

    dv "А потом я тебя встретила, на площади. В плавках."
    "Мику с Алисой опять захихикали, а я покрылся красным. {w}Мда уж... стоит поподробней узнать о том, что же здесь произошло."

    show mi smile pioneer
    show dv grin pioneer2 
    with dspr

    dv "Да ладно, форму же нашёл."
    "Алиса подмигнула мне, улыбнувшись и мы пошли дальше."
    
    hide mi
    hide dv
    with dissolve

    "Проходя мимо различных зданий я мысленно отмечал, что за все эти дни они стали мне родными. Я понимал, что сильно привык к шершавой бежевой стене столовой, потресканной краске зданий кружков, площадному покрытию, со всеми его трещинками. {w}Этот мир был абсолютно не враждебен. Да и казался ли он мне таким когда-либо?"
    
    "Солнце находилось в своём зените, но лишь едва пекло. С стороны леса наплывал каскад туч. Ветер неторопливо вел их по небосводу, раздумывая, где же устроить выброс осадков."
    
    scene ext_old_building_day
    show mi normal pioneer at left
    show dv normal pioneer2 at right
    with fade

    play music music_list["reflection_on_water"] loop fadein 2
    play ambience ambience_forest_day loop fadein 4

    play sound sfx_dinner_horn_processed volume 0.25

    "Вдалеке послышался звук горна. Ноги завели нас к тропинке в старый лагерь, и девушки, остановившись, всматривались вдаль."
    
    dv "А что было тогда, в старом лагере?"
    "Поинтересовалась Алиса, не отводя взгляд от тропинки."
    
    "Я уже было начал рассказывать, но Мику остановила меня жестом."

    mi "Я расскажу, пойдём, а то ещё обед пропустим."

    show blink
    $ renpy.pause(1.5, hard=True)

    "Мику начала рассказ о наших небезызвестных приключениях, опуская некоторые моменты, знать о которых Двачевской совсем не обязательно. За прекрасным повествующим голосом Мику я и не заметил, как мы оказались у столовой." 

    scene ext_dining_hall_near_day
    
    hide blink
    show unblink
    $ renpy.pause(1.5, hard=True)

    "Я потянул на себя дверь и предложил девушкам войти, после чего поспешил за ними."
    
    scene int_dining_hall_people_day with dissolve

    "Столовая была как всегда забита, что неудивительно – кушать всем хочется. Мы попрощались с Алисой, взяли по порции и сели за один из свободных столиков."

    show mi normal pioneer with dissolve

    "Я не мог не заметить, что Мику была очень радостной, впрочем как обычно. Но сейчас-то у нас была серьёзная проблема, которая не переставала терзать мою душу."
    
    me "Мику, почему ты такая позитивная?"
    "Спросил я, заглянув в её глаза."
    
    show mi smile pioneer with dissolve

    play music music_list["reminiscences"] loop fadein 2

    mi "Потому что, Сёма. Если нам с тобой осталось лишь два дня, то зачем тратить их на грусть?"
    "Она тепло улыбнулась мне, и я тут же позабыл о всех своих проблемах."
    
    "Всё же было в этой девушке что-то необычное, что-то позитивное, выходящее из её беззаботности и разговорчивости. Именно это и притянуло меня к ней, наверно."
    
    "С обедом было давно покончено, и я отнёс наши порции, после чего взял Мику за руку. Мы вышли из столовой."

    scene ext_dining_hall_away_sunset
    show mi normal pioneer 
    with dissolve

    mi "Семён, может прогуляемся по лесу? Тут так скучно..."
    "Мику задумчиво посмотрела в сторону тропинки."
    
    "Ну да, в лесу гораздо интереснее. Тем более небо тучами затянуло, идеально."
    
    me "Не вижу причин отказаться!"
    "Вздохнул я, и мы пошли по тропинке."
    
    scene ext_path_day with fade

    "Ветер, по дождливому договору с тучами начал набирать обороты. От очередного его дыхания Мику поёжилась, обняв мою руку и прижалась к ней. Мимо нас проходили десятки деревьев самых разных ростов и размеров, в слабых бликах солнца вдалеке переливалось озеро."
    "В этом лесу было прохладно, я бы даже сказал, холодновато, но я не ощущал дискомфорт."
    
    show mi normal pioneer with dissolve

    mi "Семён."
    "Решила начать Мику."
    mi "А кем ты был в реальной жизни?"

    "А кем я был? До встречи с ней и приезда в лагерь я был никем. Простой человек, скрывшийся за маской анонима в интернете и изредка подрабатывающий на халтурках."
    
    me "Я?"
    "Я задумчиво всмотрелся между стволов деревьев, словно пытаясь увидеть там что-то."
    me "Да никем особо, а ты?"
    
    mi "Да я тоже собственно."
    "Мику посмотрела вдаль."

    show mi sad pioneer with dspr

    mi "Музыку люблю, в музыкальную школу хожу... Ходила..."
    "Мику погрустнела."

    play music music_list["i_dont_blame_you"] loop fadein 2

    mi "Пока родители не уехали в Японию на пару недель..."

    show mi cry pioneer with dspr

    "У неё на глазах навернулись слёзы."
    mi "И так и не вернулись..."
    "Я осторожно обнял её за плечо и прижал к себе. Она немного успокоилась."

    show mi cry pioneer close with dissolve

    mi "Мне сказали что они умерли."
    "Девушка выдохнула."
    mi "И я стала жить сама по себе..."
    
    me "Всё нормально Мику, теперь у тебя есть я."
    "Я как можно добрее улыбнулся ей. Отвела взгляд..."
    
    mi "И ты остался лишь на пару дней..."
    
    me "Это будут лучшие пару дней в твоей жизни, не забывай, с меня ещё поездка на остров! – улыбнулся я и аккуратно приподнял её подбородок."
    
    show blink
    $ renpy.pause(1.5, hard=True)

    "Мику закрыла глаза и потянулась ко мне. Я не смог устоять перед этими мягкими тёплыми губами."

    $ persistent.sprite_time = "sunset"
    $ sunset_time()

    "Мы гуляли ещё около часа, пока не раздался сигнал на ужин."

    scene int_dining_hall_people_sunset

    play ambience ambience_dining_hall_full loop fadein 4

    hide blink
    show unblink
    $ renpy.pause(1.5, hard=True)
    
    "Наша скромная компания из двух человек разместилась за одним из столиков, и мы начали ужин в тишине, каждый в своих мыслях. Мику поглядывала на пристань в предвкушении, а я размышлял, как же отсюда можно выбраться?"
    
    "Девушка быстро, но аккуратно поужинала и вышла из столовой, сказав лишь: \"Буду ждать на пристани.\" Я же неторопливо доел и прошёл к выходу."

    scene ext_path_sunset with fade

    play music music_list["mystery_girl_v2"] loop fadein 2
    play ambience ambience_forest_evening loop fadein 4

    "Я аккуратно ступал по потрескавшейся плитке, наблюдая за опускавшимся солнцем, пока не услышал из леса девичий шёпот."
    
    bush "Сёмен!"
    
    "Что?"
    
    bush "Подойди сюда."
    
    "Не дай бог это опять Алиса с Ульяной что-то задумали. Могли бы хоть в последний день смены от людей отстать."
    
    scene ext_bush_sunset
    show uv normal 
    with dissolve
    
    $ unfathomable_feeling_open_image_gallery("bg", 4, 1)

    "Когда я прошёл сквозь плотную листву, я увидел перед собой девушку. Даже не просто девушку, а девушку с кошачьими ушами и хвостом."
    
    "М-да... Этот лагерь не перестаёт меня удивлять. Что завтра? Вертолёт с пиратами?"
    
    me "Привет. Не думай что удивила меня, за свою смену я многое здесь повидал. Говори, что хотела.
    Холодно произнёс я."
    
    show uv upset with dspr

    "Девочка-кошка посмотрела на меня растерянно, даже с некой обидой во взгляде."
    
    show uv normal with dspr

    uv "Ладно..."
    "Выдохнула она."
    uv "Я знаю что ты переместился сюда из другой смены. Они недавно научились так делать, но это неправильно. В общем, после этой смены все около пятнадцати тысяч миров захлопнутся, отрываясь от выхода." 
    uv "Из этого лагеря можно выбраться, достаточно сесть в автобус, но не все девушки смогут. Ты можешь их спасти."
    
    me "Какие ещё девушки?"
    "Удивлённо спросил я."
    
    uv "У каждой из пяти девушек: Слави, Алисы, Ульяны, Лены, Мику, есть свои реальности, в которых они настоящие. Также у них есть куча копий в мирах других настоящих людей, а ещё есть миры, полностью состоящие из копий." 
    uv "Но это очень долго объяснять, главное – они должны сесть в автобус с тобой. Поэтому ты должен собрать их всех вместе и уехать из этого лагеря, тогда он исчезнет навсегда."
    
    me "Я ничего никому не должен."
    "Сказал я грубым голосом и начал отходить."
    
    "\"Хорошая попытка, лагерь\" - заметил я про себя, выходя из зарослей."

    scene ext_path_sunset with dissolve

    "Странно, но слова этой кошко-девушки совсем не задели меня. Прямо ни капли. Я ещё раз кинул взгляд на солнце, которое медленно, но верно подползало к горизонту, раскидывая свои янтарные отблески по округе."
    
    "Вспомнив, что моя любимая ждёт меня около пяти минут, я быстро добежал до домиков и мигом натянул плавки."

    show blink
    window hide 
    $ renpy.pause(1.5, hard=True)

    scene ext_boathouse_sunset

    play music music_list["forest_maiden"] loop fadein 2
    play ambience ambience_lake_shore_evening loop fadein 4

    hide blink
    show unblink
    $ renpy.pause(1.5, hard=True)
    window show

    "Вода лениво подползала, заворачивая под собой песок, а потом снова, также неспешно отступала, собираясь с новыми силами."
    
    "Засмотревшись на это противостояние песка и воды, Мику совсем не заметила, как рядом с ней появился Семён. Он аккуратно поцеловал её в шею, обжигая своим дыханием, после чего жестом пригласил в лодку, которая качалась прямо под ногами девушки."
    "Недолго мечтательно посмотрев в сторону возлюбленного, девушка осторожно села на дощечку, которая служила сидением."
    
    "Парень скрылся в здании пристани и уже через несколько секунд выпорхнул оттуда с парой вёсел."

    scene mi_boat_sunset with dissolve

    $ unfathomable_feeling_open_image_gallery("cg", 3, 4)

    "Во время их плавания Мику внимательно смотрела в сторону исчезающего светила. Семён же был полностью сосредоточен на гребле: всё-таки его мышцы довольно долгое время не ощущали такой нагрузки." 
    "Хотя он всем своим видом пытался показать, что всё нормально, испарина на его лбу и снижение темпа движения выдавали его с головой. Внутри себя Семён молился, чтобы эта прогулка на воде закончилась как можно быстрее." 
    "А ведь ему ещё обратно сегодня плыть. Или не сегодня? Парень стрельнул глазами в сторону Мику и они встретились взглядами."

    mi "Тебе не тяжело?"
    "Заботливо спросила девушка."
    
    me "Если только совсем немного."
    "Произнес Семён сквозь зубы и улыбнулся. Какой тяжести ему стоила эта улыбка."

    "Мику обернулась, посмотрев, сколько осталось до острова, после чего сняла обувь и осторожно вышла из лодки."
    
    scene ext_beach_sunset with fade

    $ unfathomable_feeling_open_image_gallery("bg", 3, 4)
    
    "Наш герой последовал её примеру и через минуту они уже сидели на берегу рядом с привязанной лодкой и смотрели на закат."
    
    "Мику положила свою голову на плечо Семёну и её хвосты спали вниз, на песок. Мику зарывалась в него одной из своих ножек, пропуская песчинки между пальцев."
    
    show mi normal pioneer with dissolve

    "Снова засмотревшись на речные волны, девушка произнесла:"

    mi "Может, искупаемся?"

    me "Конечно!"
    "Семён немного отдохнул от недавнего марафона и был не прочь освежиться."

    hide mi with dissolve

    "Пара начала раздеваться, вешая вещи на обломанный сук ближайшего дерева."
    
    scene ext_beach_water_sunset with dissolve

    $ unfathomable_feeling_open_image_gallery("bg", 3, 4)
    
    "Семён неторопливо прошёл к воде, аккуратно опустив ногу в реку. Шаг. Ещё один. Парень уже по колено в воде, но никак не может решиться полностью отдаться этой заманчивой прохладе."

    "Внезапно он потерял равновесие и сделал шаги навстречу реке, лишь бы только устоять. Но его нога скользит обо что-то и Семён оказывается в реке с головой. Он выныривает лишь с одной целью: посмотреть на причину своего падения."
    
    show mi laugh swim with dissolve

    "Виновница бесстыдно смеётся и будет подвержена самым ужасным пыткам. Парень зачерпывает горсть воды и отправляет её на прекрасное тело обидчицы."
    
    show mi smile swim with dspr

    "Ледяная вода обжигает кожу Мику, и за первыми ощущениями следует пронзительный девичий визг. Семён закрывает уши и отворачивается, и именно этот момент выбирает девушка для нанесения ответного удара."
    'Старая добрая "бомбочка" обливает всё в радиусе десяти метров.'
    
    "Брызги ложатся на лодку, на повешенную одежду, большая часть воды попадает и на парня, посмевшего ответить на легенький подкол Мику."

    "Между влюблёнными началась ожесточённая схватка не на жизнь, а на смерть."

    scene ext_beach_sunset with fade

    play music music_list["memories"] loop fadein 2

    "Уставший Семён сел на берег, окунув ноги в воду и наблюдал за плескавшейся девушкой. Он почувствовал, что его что-то щекочет. "
    "Он опустил свой взор на кристально чистую водную гладь и заметил стайку маленьких рыбок, плавающих возле его ноги и иногда щипающих её."
    
    "Парень выдохнул и лёг на песок, скрестив руки в замке на затылке. Солнце уже давно село, оставив на месте своего исчезновения пару багровых пятен, чья учесть была также предрешена."
    
    "Стайка рыбёшек в спешке отплыла, опасаясь быть раздавленной лёгкой поступью девушки. Мику вышла из воды и легла на грудь Семёну, раскинув свои хвостики в разные стороны."

    scene epilogue_mi_1 with dissolve

    "Грудь парня то поднималась, то возвращалась в своё изначальное положение. От этого девушке становилось очень спокойно, и хотелось просто остаться так лежать, и забыть обо всём..."
    
    "Дыхание Семёна стало размеренным и Мику ткнула его в бок."

    mi "Ты чего? Спать вздумал?
    С легкой насмешкой спросила Мику."
    
    me "Извини, просто когда я рядом с тобой, так хорошо становится.
    Семён откинул голову и посмотрел на звёзды."
    
    "Через несколько секунд молчания девушка всё-таки решилась."
    
    mi "А хочешь, я буду ещё ближе?"
    "Глаза девушки игриво сверкнули в лунном свете."

    "К горлу Семёна подошёл комок. Он не мог не согласиться, не отказаться от подобного предложения. Понимая, что своим промедлением он обижает девушку, парень притянул Мику к себе и прильнул к её губам."

    show blink
    stop ambience fadeout 2
    $ renpy.pause(2, hard=True)

    "И то что произошло сегодняшней ночью на острове останется тайной для всех, кроме наших главных героев. Единственное, что можно сказать с точностью - они предались сладостному забвению, отодвинув любовь и нежность на задний план."
    "Они открыли новый, самый действенный способ признаться друг другу в чувствах и ушли в объятья страсти."
    
    "Им действительно было это необходимо, ведь для них прошло всего несколько дней счастья, и это смягчит их завтрашнюю разлуку. Или только им так кажется. Время покажет..."

    jump unfathomable_feeling_day_7