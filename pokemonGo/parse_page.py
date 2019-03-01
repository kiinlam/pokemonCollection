#使用pyQuery解析html页面，提取数据

from pyquery import PyQuery as pq

def get_items_text(nodes):
    """获取节点中的文本"""
    return [v.text() for v in nodes.items()]


def parse(html):
    _ = pq(html)('.pokemon-detail')

    data = dict()

    # 属性
    types = _('.pokemon-type__type')
    data['type'] = []
    for item in types.items():
        item = {
            'id': item.find('a').attr('href').replace('/play/pokedex/', '').replace('#result', ''),
            'name': item.text()
        }
        data['type'].append(item)

    # 弱点
    weakness = _('.pokemon-weakness__items .pokemon-weakness__btn')
    data['weakness'] = []
    for item in weakness.items():
        item = {
            'id': item.find('a').attr('href').replace('/play/pokedex/', '').replace('#result', ''),
            'name': item.text()
        }
        data['weakness'].append(item)

    # 分类
    data['category_name'] = ','.join(get_items_text(_('.pokemon-info__category .pokemon-info__value')))

    # 性别
    gender = map(lambda x: x.replace('/play/resources/pokedex/img/icon_', '').replace('.png', ''),
                 [gender.attr('src') for gender in _('.pokemon-info__gender img').items()])
    data['gender_name'] = list(gender)

    # 特性
    data['abilities_name'] = get_items_text(_('.pokemon-info__abilities .pokemon-info__value'))

    # 特性说明
    data['ability_info'] = get_items_text(_('.pokemon-info__ability_info .pokemon-info__value--body'))

    # 图鉴介绍
    storys = get_items_text(_('.pokemon-story__body'))
    story = []
    for item in storys:
        if item not in story:
            story.append(item)

    data['story'] = story

    # 能力层级
    data['status'] = []
    for item in _('.pokemon-stats__wrapper-status .pokemon-status').items():
        status_title = item.find('.pokemon-status__title').text()
        status_value = len(item.find('.pokemon-status__scale').filter(lambda k, v: 'appear' in pq(v).outerHtml()))
        data['status'].append([status_title, status_value])

    # 形态
    # 主id相同，副id不同，为不同的形态样子，对应不同的进化

    # 进化
    # 主id加1，副id相同
    def each_evolution(k, v):
        text = pq(v).find('.pokemon-evolution-box__no').text()
        data['evolution'].append(text)

    data['evolution'] = []
    _('.pokemon-evolution .pokemon-evolutionlevel').each(each_evolution)

    print(data)
    return data


def main():
    html = """
    <!doctype html>
    <html lang="zh-cmn-Hans-CN">
        <head prefix="og: http://ogp.me/ns# fb: http://ogp.me/ns/fb# website: http://ogp.me/ns/website#">
            <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="csrf-token" content="">
    <title>妙蛙种子 | 宝可梦图鉴 | The official Pokémon Website in China</title>
    <meta name="keywords" content="妙蛙种子,宝可梦,精灵宝可梦,Pokemon,宝可梦图鉴">
    <meta name="description" content="会看到它在太阳底下睡午觉的样子。在沐浴了充足的阳光后，它背上的种子就会茁壮成长。">
    <meta property="og:title" content="妙蛙种子 | 宝可梦图鉴 | The official Pokémon Website in China">
    <meta property="og:description" content="会看到它在太阳底下睡午觉的样子。在沐浴了充足的阳光后，它背上的种子就会茁壮成长。">
    <meta property="og:image" content="https://cn.portal-pokemon.com/play/resources/pokedex/img/pm/cf47f9fac4ed3037ff2a8ea83204e32aff8fb5f3.png">
    <meta property="og:type" content="article">
    <meta property="og:site_name" content="The official Pokémon Website in China">
    <meta name="twitter:card" content="summary_large_image">
    <meta name="format-detection" content="telephone=no">
    <link rel="canonical" href="https://cn.portal-pokemon.com/play/pokedex/001">
    <link rel="alternate" href="https://cn.portal-pokemon.com/play/pokedex/001" hreflang="zh-cn">
    <link rel="alternate" href="https://tw.portal-pokemon.com/play/pokedex/001" hreflang="zh-tw">
    <link rel="alternate" href="https://hk.portal-pokemon.com/play/pokedex/001" hreflang="zh-hk">
    <link rel="alternate" href="https://ph.portal-pokemon.com/play/pokedex/001" hreflang="en-ph">
    <link rel="alternate" href="https://my.portal-pokemon.com/play/pokedex/001" hreflang="ms">
    <link rel="alternate" href="https://in.portal-pokemon.com/play/pokedex/001" hreflang="en-in">
    <link rel="alternate" href="https://id.portal-pokemon.com/play/pokedex/001" hreflang="id">
    <link rel="alternate" href="https://vn.portal-pokemon.com/play/pokedex/001" hreflang="vi">
    <link rel="alternate" href="https://th.portal-pokemon.com/play/pokedex/001" hreflang="th">
    <link rel="alternate" href="https://sg.portal-pokemon.com/play/pokedex/001" hreflang="en-sg">
    <link rel="alternate" href="https://www.portal-pokemon.com/play/pokedex/001" hreflang="x-default">
    <link rel="stylesheet" href=  "/css/style.css"  >
    <link rel="stylesheet" type="text/css" href="/play/resources/pokedex/css/app.css">
    <!-- Google Tag Manager -->
    <script>(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':
    new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],
    j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
    'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
    })(window,document,'script','dataLayer','GTM-554S3MJ');</script>
    <!-- End Google Tag Manager -->    </head>
        <body>
            <!-- Google Tag Manager (noscript) -->
            <noscript><iframe src="https://www.googletagmanager.com/ns.html?id=GTM-554S3MJ"
            height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>
            <!-- End Google Tag Manager (noscript) -->
            <header class="global-header" role="banner">
    		<div class="global-header__body">
    			<div class="global-header__title">
                <h1 class="global-header__site-name"><a href="/"><img src="/img/common/logo.png" alt="Pokemon" width="130"></a></h1>
    			</div>
    			<nav class="nav-global" role="navigation">
    				<div class="nav-global__body">
    					<ul class="nav-global__list">
                            <li class="nav-global__item"><a class="nav-global__item--anime" href="/anime/"><span>电视动画系列</span></a></li>
                            <li class="nav-global__item"><a class="nav-global__item--movie" href="/movie/"><span>电影</span></a></li>
                            <li class="nav-global__item"><a class="nav-global__item--goods" href="/goods/"><span>商品</span></a></li>
                            <li class="nav-global__item"><a class="nav-global__item--app" href="/apps/"><span>应用程序</span></a></li>
                            <li class="nav-global__item"><a class="nav-global__item--game" href="/game/"><span>游戏</span></a></li>
                            <li class="nav-global__item"><a class="nav-global__item--card" href="/card/"><span>卡牌游戏</span></a></li>
                            <li class="nav-global__item"><a class="nav-global__item--event" href="/event/"><span>活动</span></a></li>
                            <li class="nav-global__item nav-global__item--what"><a href="/play/pokedex"><span>宝可梦图鉴</span></a></li>
    					</ul>
    					<div class="global-header__sp-close visible-xs">
    						<button>
    							<span>Close</span>
    						</button>
    					</div>
    				</div>
    			</nav>
    		</div>
    		<div class="global-header__sp-menu visible-xs">
    			<button>
    				<span></span>
    				<span></span>
    				<span></span>
    			</button>
    		</div>
    	</header>        <div class="contents pokemon-detail-contents">
        <div class="pokemon-detail">
            <div class="pokemon-detail__header">
                <div class="pokemon-detail__header__inner">
                    <span class="size-20"><a class="pokemon-detail__header__back-to-top" href="/play/pokedex">宝可梦图鉴</a></span>
                </div>
            </div>
            <div class="pokemon-detail__slider">
                <div class="pokemon-slider">
                                        <div class="pokemon-slider__wrapper pokemon-slider__wrapper--left non-visible">
                                    </div>
                    <div class="pokemon-slider__main">
                        <p class="pokemon-slider__main-no size-28">001</p>
                        <p class="pokemon-slider__main-name size-35">妙蛙种子</p>
                        <p class="pokemon-slider__main-subname size-20"></p>
                    </div>
                                                            <div class="pokemon-slider__wrapper pokemon-slider__wrapper--right">
                            <a href="/play/pokedex/002">
                                                <img class="pokemon-slider__arrow pokemon-slider__arrow--right hover_image" src="/play/resources/pokedex/img/arrow_right_btn.png">
                        </a>
                        <span class="pokemon-slider__sub-name pokemon-slider__sub-name--right size-15">妙蛙草</span>
                        <span class="pokemon-slider__sub-no pokemon-slider__sub-no--right size-14">002</span>
                                    </div>
                </div>
            </div>
            <div class="pokemon-detail__profile">
                <div class="pokemon-main">
                    <div class="pokemon-main__center">
                        <div class="pokemon-img">
                            <img class="pokemon-img__back" src="/play/resources/pokedex/img/pokemon_bg.png">
                            <img class="pokemon-img__blur" src="/play/resources/pokedex/img/pokemon_circle_bg.png">
                            <img class="pokemon-img__front" src="/play/resources/pokedex/img/pm/cf47f9fac4ed3037ff2a8ea83204e32aff8fb5f3.png">
                        </div>
                    </div>
                    <div class="pokemon-main__upper-left">
                        <div class="pokemon-type__title size-20">属性</div>
                            <div class="pokemon-type">

                                                                                                                             <div class="pokemon-type__type pokemon-type__type--grass pokemon-type__type--has_second size-14">
                                            <a href="/play/pokedex/grass#result">
                                                <span>草</span>
                                            </a>
                                        </div>
                                                                                                                                    <div class="pokemon-type__type pokemon-type__type--poison pokemon-type__type--second size-14">
                                            <a href="/play/pokedex/poison#result">
                                            <span>毒</span>
                                            </a>
                                        </div>
                                                                                                             </div>
                    </div>
                    <div class="pokemon-main__bottom-left">
                        <div class="pokemon-weakness__title size-20">弱点</div>
                        <div class="pokemon-weakness">
                            <div class="pokemon-weakness__items">
                                                                                                                <div class="pokemon-weakness__btn pokemon-weakness__btn--flying size-14">
                                        <a href="/play/pokedex/flying#result">
                                            <!-- <span>飞行</span> -->
                                            <span>飞行</span>
                                        </a>
                                    </div>
                                                                                                                                                <div class="pokemon-weakness__btn pokemon-weakness__btn--fire size-14">
                                        <a href="/play/pokedex/fire#result">
                                            <!-- <span>火</span> -->
                                            <span>火</span>
                                        </a>
                                    </div>
                                                                                                                                                <div class="pokemon-weakness__btn pokemon-weakness__btn--psychic pokemon-weakness__btn--second-line size-14">
                                        <a href="/play/pokedex/psychic#result">
                                            <!-- <span>超能力</span> -->
                                            <span>超能力</span>
                                        </a>
                                    </div>
                                                                                                                                                <div class="pokemon-weakness__btn pokemon-weakness__btn--ice pokemon-weakness__btn--second-line size-14">
                                        <a href="/play/pokedex/ice#result">
                                            <!-- <span>冰</span> -->
                                            <span>冰</span>
                                        </a>
                                    </div>
                                                                                                            </div>
                        </div>
                    </div>
                    <div class="pokemon-main__right">
                        <div class="pokemon-info" v-cloak>
                            <transition name="pokemon-info__fade">
                                <div class="pokemon-info--inner" v-if="!ability_info_f && !ability_info_s && !ability_info_t">
                                    <div class="pokemon-info__height">
                                        <span class="pokemon-info__title size-14">身高</span>
                                        <span class="pokemon-info__value size-14">0.7 m</span>
                                    </div>
                                    <div class="pokemon-info__category">
                                        <span class="pokemon-info__title size-14">分类</span>
                                        <span class="pokemon-info__value size-14"><span>种子宝可梦</span></span>
                                    </div>
                                    <div class="pokemon-info__weight">
                                        <span class="pokemon-info__title size-14">体重</span>
                                        <span class="pokemon-info__value size-14">6.9 kg</span>
                                    </div>
                                    <div class="pokemon-info__gender">
                                        <span class="pokemon-info__title size-14">性别</span>
                                        <span class="pokemon-info__value size-14">
                                                                                        <img class="pokemon-info__gender-icon" src="/play/resources/pokedex/img/icon_male.png" alt="">
                                                <span class="pokemon-info__gender-separator">/</span>
                                                <img class="pokemon-info__gender-icon" src="/play/resources/pokedex/img/icon_female.png" alt="">
                                                                                </span>
                                    </div>
                                                                    <div class="pokemon-info__abilities">
                                        <span class="pokemon-info__title size-14">特性</span>
                                                                                                                    <span class="pokemon-info__value size-14">
                                                茂盛
                                                <img class="pokemon-info__question-icon" src="/play/resources/pokedex/img/icon_question.png" v-on:click="showAbilityText(0, true)">
                                            </span>
                                                                                                                </div>
                                                                </div>
                            </transition>
                                                    <transition name="pokemon-info__fade">
                                                                                        <div class="pokemon-info__ability_info" v-if="ability_info_f" v-show="id === 0">
                                                                    <span class="pokemon-info__title size-14">特性</span>
                                        <img class="pokemon-info__ability_info--close_btn" src="/play/resources/pokedex/img/close_btn.png" v-on:click="showAbilityText(0, false)">
                                            <span class="pokemon-info__value pokemon-info__value--title size-18">茂盛</span>
                                            <span class="pokemon-info__value pokemon-info__value--body size-14"><span>ＨＰ减少的时候，草属性的招式威力会提高。</span></span>
                                    </div>
                                                                                    </transition>
                        </div>
                    </div>
                </div>
            </div>
            <div class="pokemon-detail__stats">
                <div class="pokemon-stats">
                    <div class="pokemon-stats__story-wrapper">
                      <div class="pokemon-stats__story-inner">
                          <div class="pokemon-story" v-cloak>
                              <div class="pokemon-story__header">
                                  <span class="pokemon-story__title size-20">图鉴版本</span>
                                  <div class="pokemon-story__icon-wrapper">
                                      <img class="pokemon-story__icon" :src="ballImage1" alt="" @click="whichStory = !whichStory">
                                      <img class="pokemon-story__icon" :src="ballImage2" alt="" @click="whichStory = !whichStory">
                                  </div>
                              </div>
                              <p class="pokemon-story__body size-14" v-if="whichStory">
                                  <span>会看到它在太阳底下睡午觉的样子。在沐浴了充足的阳光后，它背上的种子就会茁壮成长。</span>
                              </p>
                              <p class="pokemon-story__body size-14" v-if="!whichStory">
                                  <span>会看到它在太阳底下睡午觉的样子。在沐浴了充足的阳光后，它背上的种子就会茁壮成长。</span>
                              </p>
                          </div>
                      </div>
                    </div>
                    <div class="pokemon-stats__status-wrapper">
                        <div class="pokemon-stats__title size-20">
                            <span>能力</span>
                        </div>
                        <div class="pokemon-stats__wrapper-status">
                            <div class="pokemon-status__block">
                                <div class="pokemon-status">
                                    <div class="pokemon-status__scale-box">
                            <span class="pokemon-status__scale"></span>
                                    <span class="pokemon-status__scale"></span>
                                    <span class="pokemon-status__scale"></span>
                                    <span class="pokemon-status__scale"></span>
                                    <span class="pokemon-status__scale"></span>
                                    <span class="pokemon-status__scale"></span>
                                    <span class="pokemon-status__scale"></span>
                                    <span class="pokemon-status__scale"></span>
                                    <span class="pokemon-status__scale d2" v-bind:class="{ appear: isAppear }"></span>
                                    <span class="pokemon-status__scale d1" v-bind:class="{ appear: isAppear }"></span>
                </div>                                <div class="pokemon-status__title size-10"><span>HP</span></div>
                                </div>
                                <div class="pokemon-status">
                                    <div class="pokemon-status__scale-box">
                            <span class="pokemon-status__scale"></span>
                                    <span class="pokemon-status__scale"></span>
                                    <span class="pokemon-status__scale"></span>
                                    <span class="pokemon-status__scale"></span>
                                    <span class="pokemon-status__scale"></span>
                                    <span class="pokemon-status__scale"></span>
                                    <span class="pokemon-status__scale"></span>
                                    <span class="pokemon-status__scale d3" v-bind:class="{ appear: isAppear }"></span>
                                    <span class="pokemon-status__scale d2" v-bind:class="{ appear: isAppear }"></span>
                                    <span class="pokemon-status__scale d1" v-bind:class="{ appear: isAppear }"></span>
                </div>                                <div class="pokemon-status__title size-10"><span>攻击</span></div>
                                </div>
                                <div class="pokemon-status">
                                    <div class="pokemon-status__scale-box">
                            <span class="pokemon-status__scale"></span>
                                    <span class="pokemon-status__scale"></span>
                                    <span class="pokemon-status__scale"></span>
                                    <span class="pokemon-status__scale"></span>
                                    <span class="pokemon-status__scale"></span>
                                    <span class="pokemon-status__scale"></span>
                                    <span class="pokemon-status__scale"></span>
                                    <span class="pokemon-status__scale"></span>
                                    <span class="pokemon-status__scale d2" v-bind:class="{ appear: isAppear }"></span>
                                    <span class="pokemon-status__scale d1" v-bind:class="{ appear: isAppear }"></span>
                </div>                                <div class="pokemon-status__title size-10"><span>防御</span></div>
                                </div>
                            </div>
                            <div class="pokemon-status__block">
                                <div class="pokemon-status">
                                    <div class="pokemon-status__scale-box">
                            <span class="pokemon-status__scale"></span>
                                    <span class="pokemon-status__scale"></span>
                                    <span class="pokemon-status__scale"></span>
                                    <span class="pokemon-status__scale"></span>
                                    <span class="pokemon-status__scale"></span>
                                    <span class="pokemon-status__scale"></span>
                                    <span class="pokemon-status__scale"></span>
                                    <span class="pokemon-status__scale d3" v-bind:class="{ appear: isAppear }"></span>
                                    <span class="pokemon-status__scale d2" v-bind:class="{ appear: isAppear }"></span>
                                    <span class="pokemon-status__scale d1" v-bind:class="{ appear: isAppear }"></span>
                </div>                                <div class="pokemon-status__title size-10"><span>特攻</span></div>
                                </div>
                                <div class="pokemon-status">
                                    <div class="pokemon-status__scale-box">
                            <span class="pokemon-status__scale"></span>
                                    <span class="pokemon-status__scale"></span>
                                    <span class="pokemon-status__scale"></span>
                                    <span class="pokemon-status__scale"></span>
                                    <span class="pokemon-status__scale"></span>
                                    <span class="pokemon-status__scale"></span>
                                    <span class="pokemon-status__scale"></span>
                                    <span class="pokemon-status__scale"></span>
                                    <span class="pokemon-status__scale d2" v-bind:class="{ appear: isAppear }"></span>
                                    <span class="pokemon-status__scale d1" v-bind:class="{ appear: isAppear }"></span>
                </div>                                <div class="pokemon-status__title size-10"><span>特防</span></div>
                                </div>
                                <div class="pokemon-status">
                                    <div class="pokemon-status__scale-box">
                            <span class="pokemon-status__scale"></span>
                                    <span class="pokemon-status__scale"></span>
                                    <span class="pokemon-status__scale"></span>
                                    <span class="pokemon-status__scale"></span>
                                    <span class="pokemon-status__scale"></span>
                                    <span class="pokemon-status__scale"></span>
                                    <span class="pokemon-status__scale"></span>
                                    <span class="pokemon-status__scale d3" v-bind:class="{ appear: isAppear }"></span>
                                    <span class="pokemon-status__scale d2" v-bind:class="{ appear: isAppear }"></span>
                                    <span class="pokemon-status__scale d1" v-bind:class="{ appear: isAppear }"></span>
                </div>                                <div class="pokemon-status__title size-10"><span>速度</span></div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>

            <div class="pokemon-detail__style">
                <div class="pokemon-style__title size-20">
                    <span>样子</span>
                </div>

                                <div class="pokemon-style pokemon-style--empty">
            <div class="pokemon-style__boxes-wrapper">
                <div class="pokemon-style__boxes">
                    <div class="pokemon-style__boxes-inner">
                                                                            <span class="size-14">没有不同的样子</span>
                                                                </div>
                </div>
            </div>
        </div>                    </div>
            <div class="pokemon-detail__evolutions">
            <div class="pokemon-evolution bg-x-22 pokemon-evolution--3
    pokemon-evolution--h
    ">
            <div class="pokemon-evolution__inner innerNormalStyle innerSimpleStyle">
                <div class="pokemon-evolution__title size-20">
                <span>进化</span>
            </div>
            <div class="pokemon-evolution-contents">
                <div class="pokemon-evolution-contents_flow">
                                            <div class="pokemon-evolutionlevel">
                                                                                                                                                                                            <div class="pokemon-evolution-itembox">
                                                                                                        <a href="/play/pokedex/001">

                                                                            <div class="pokemon-evolution-item__image">
                                            <img class="pokemon-evolution-box__image" src="/play/resources/pokedex/img/pm/cf47f9fac4ed3037ff2a8ea83204e32aff8fb5f3.png">
                                        </div>
                                        <div class="pokemon-evolution-item__info">
                                                                                <p class="pokemon-evolution-box__no size-14">001</p>
                                            <p class="pokemon-evolution-item__info-name size-14">妙蛙种子</p>
                                            <p class="pokemon-evolution-item__info-subname size-10"></p>
                                            <div class="pokemon-evolution-box__types">
                                                                                                                                                    <div class="pokemon-evolution-item__info-type pokemon-evolution-box__type--grass size-12">
                                                            <div><span>草</span></div>
                                                        </div>
                                                                                                        <div class="pokemon-evolution-item__info-type pokemon-evolution-box__type--poison size-12">
                                                            <div><span>毒</span></div>
                                                        </div>
                                                                                                                                        </div>
                                        </div>
                                                                                                    </a>
                                                                                                                                        <div class="pokemon-evolution-item__narrow">
                                                                                <div class="pokemon-evolution__arrow-wrapper">
                                                <img class="pokemon-evolution__arrow" src="/play/resources/pokedex/img/arrow_down.png">
                                            </div>
                                        </div>
                                                                                            </div>
                                                                                            </div>
                                                <div class="pokemon-evolutionlevel">
                                                                                                                                                                                            <div class="pokemon-evolution-itembox">
                                                                                                        <a href="/play/pokedex/002">

                                                                            <div class="pokemon-evolution-item__image">
                                            <img class="pokemon-evolution-box__image" src="/play/resources/pokedex/img/pm/3245e4f8c04aa0619cb31884dbf123c6918b3700.png">
                                        </div>
                                        <div class="pokemon-evolution-item__info">
                                                                                <p class="pokemon-evolution-box__no size-14">002</p>
                                            <p class="pokemon-evolution-item__info-name size-14">妙蛙草</p>
                                            <p class="pokemon-evolution-item__info-subname size-10"></p>
                                            <div class="pokemon-evolution-box__types">
                                                                                                                                                    <div class="pokemon-evolution-item__info-type pokemon-evolution-box__type--grass size-12">
                                                            <div><span>草</span></div>
                                                        </div>
                                                                                                        <div class="pokemon-evolution-item__info-type pokemon-evolution-box__type--poison size-12">
                                                            <div><span>毒</span></div>
                                                        </div>
                                                                                                                                        </div>
                                        </div>
                                                                                                    </a>
                                                                                                                                        <div class="pokemon-evolution-item__narrow">
                                                                                <div class="pokemon-evolution__arrow-wrapper">
                                                <img class="pokemon-evolution__arrow" src="/play/resources/pokedex/img/arrow_down.png">
                                            </div>
                                        </div>
                                                                                            </div>
                                                                                            </div>
                                                <div class="pokemon-evolutionlevel">
                                                                                                                                                                                            <div class="pokemon-evolution-itembox">
                                                                                                        <a href="/play/pokedex/003">

                                                                            <div class="pokemon-evolution-item__image">
                                            <img class="pokemon-evolution-box__image" src="/play/resources/pokedex/img/pm/0186d64c5773c8d3d03cd05dc79574b2d2798d4f.png">
                                        </div>
                                        <div class="pokemon-evolution-item__info">
                                                                                <p class="pokemon-evolution-box__no size-14">003</p>
                                            <p class="pokemon-evolution-item__info-name size-14">妙蛙花</p>
                                            <p class="pokemon-evolution-item__info-subname size-10"></p>
                                            <div class="pokemon-evolution-box__types">
                                                                                                                                                    <div class="pokemon-evolution-item__info-type pokemon-evolution-box__type--grass size-12">
                                                            <div><span>草</span></div>
                                                        </div>
                                                                                                        <div class="pokemon-evolution-item__info-type pokemon-evolution-box__type--poison size-12">
                                                            <div><span>毒</span></div>
                                                        </div>
                                                                                                                                        </div>
                                        </div>
                                                                                                    </a>
                                                                                                                        </div>
                                                                                            </div>
                                        </div>
            </div>
        </div>
    </div>
            </div>

                    <div class="pokemon-detail__sns">
                <div class="article-sns">
                    <ul class="article-sns__body">
                                                <li class="article-sns__element">
                                <a href="http://service.weibo.com/share/share.php?url=https%3A%2F%2Fcn.portal-pokemon.com%2Fplay%2Fpokedex%2F001&title=%E5%A6%99%E8%9B%99%E7%A7%8D%E5%AD%90+%7C+%E5%AE%9D%E5%8F%AF%E6%A2%A6%E5%9B%BE%E9%89%B4+%7C+The+official+Pok%C3%A9mon+Website+in+China&pic=https%3A%2F%2Fcn.portal-pokemon.com%2Fplay%2Fresources%2Fpokedex%2Fimg%2Fpm%2Fcf47f9fac4ed3037ff2a8ea83204e32aff8fb5f3.png&searchPic=false" target="_blank">
                                    <img src="/play/resources/pokedex/img/icon_share-weibo.png" width="30" alt="weibo">
                                </a>
                            </li>
                            <li class="article-sns__element">
                                <a href="http://qr.liantu.com/api.php?text=https%3A%2F%2Fcn.portal-pokemon.com%2Fplay%2Fpokedex%2F001" target="_blank">
                                    <img src="/play/resources/pokedex/img/icon_share-weixin.png" width="30" alt="weixin">
                                </a>
                            </li>
                            <li class="article-sns__element">
                                <a href="http://share.v.t.qq.com/index.php?c=share&amp;a=index&amp;url=https%3A%2F%2Fcn.portal-pokemon.com%2Fplay%2Fpokedex%2F001&title=%E5%A6%99%E8%9B%99%E7%A7%8D%E5%AD%90+%7C+%E5%AE%9D%E5%8F%AF%E6%A2%A6%E5%9B%BE%E9%89%B4+%7C+The+official+Pok%C3%A9mon+Website+in+China" target="_blank">
                                    <img src="/play/resources/pokedex/img/icon_share-qq.png" width="30" alt="qq">
                                </a>
                            </li>
                                        </ul>
                </div>
            </div>
            <div class="pokemon-detail__back-to-top">
                <div class="pokemon-back-to-top">
                    <a href="/play/pokedex">
                        <div class="pokemon-back-to-top__button size-14">
                            <span>返回Pokédex</span>
                        </div>
                    </a>
                </div>
            </div>
        </div>
    </div>

            <footer class="global-footer" role="contentinfo">
    	<div class="global-footer__upper">
    		<div class="global-footer__official--title visible-xs">
    			官方帐号
    		</div>
    		<div class="global-footer__upper--body">
    			<div class="global-footer__official">
    				<div class="global-footer__official--title hidden-xs">
    					官方帐号
    				</div>
    				<ul class="global-footer__official--list">
    									<li><a href="http://weibo.com/u/6305628151" target="_blank">
    										 <img src="/assets_c/2017/11/SNS_weibo-thumb-132x132-8009.png" width="66" alt="
    											微博
    											">
    										</a></li>
    									<li><a href="/upload/cn/qrcode_for_gh_8a90caea89bd_258.jpg" target="_blank">
    										 <img src="/assets_c/2017/11/SNS_wechat-thumb-132x132-8010.png" width="66" alt="
    											微信
    											">
    										</a></li>
    									<li><a href="http://v.qq.com/vplus/38f05872d099d7cc3d9d36e561cdbe5c/videos" target="_blank">
    										 <img src="/assets_c/2017/11/SNS_tencentwedio%20%281%29-thumb-132x132-11102.png" width="66" alt="
    											腾讯视频
    											">
    										</a></li>
    				</ul>
    			</div>
    		</div>
    	</div>
    	<div class="global-footer__lower">
    		<div class="global-footer__lower--body">
    			<div class="global-footer__links" role="complementary">
    				<ul>
    					<li><a href="/about/">
    						精灵宝可梦是什么？
    						</a></li>
    					<li><a href="/termofuse/">
    						使用条款
    						</a></li>
    					<li><a href="/sitemap/">
    						网站地图
    						</a></li>
    				</ul>
    			</div>
    			<div class="global-footer__country"> <a href="/country/"> <span>
    				中国
    				</span> </a> </div>
    			<div class="global-footer__copyright"> <small> &copy;2018 Pokémon. &copy;1995 - 2018 Nintendo/Creatures Inc./GAME FREAK inc.<br>
    				&copy;1997 Nintendo, Creatures, GAME FREAK, TV Tokyo, ShoPro, JR Kikaku. &copy;Pokémon. TM and &reg; are trademarks of Nintendo. </small> </div>
    		</div>
    	</div>
    </footer>    <script src="/play/resources/pokedex/js/app.js"></script>
        <script src="/play/resources/pokedex/js/pokemon-detail.js"></script>
    <script src=  "/js/baser.min.js"  ></script>
    <script src=  "/js/slick.min.js"  ></script>
    <script src=  "/js/script_common.js"  ></script>    </body>
    </html>
    """
    parse(html)


if __name__ == "__main__":
    main()
