html = """
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <meta charset="utf-8"/>
    <title>Аптека "БАМ" – Результати пошуку</title>
	<link href="/favicon.ico" type="image/x-icon" rel="icon"/><link href="/favicon.ico" type="image/x-icon" rel="shortcut icon"/>
    
	<link rel="stylesheet" href="/css/jquery.formstyler.min.css"/>
	<link rel="stylesheet" href="/css/jquery.fancybox.css"/>
	<link rel="stylesheet" href="/css/jquery-ui.min.css"/>
	<link rel="stylesheet" href="/css/jquery.mCustomScrollbar.min.css"/>
	<link rel="stylesheet" href="/css/select2.css"/>
	<link rel="stylesheet" href="/css/main.min.css?v=2.10"/>

    	<link href="/img/apple-touch-icon.png" rel="apple-touch-icon" type="image/x-icon"/>	<link href="/img/apple-touch-icon-ipad.png" rel="apple-touch-icon" type="image/x-icon" sizes="72x72"/>	<link href="/img/apple-touch-icon-iphone4.png" rel="apple-touch-icon" type="image/x-icon" sizes="114x114"/>    <meta name="og:image" content="/img/image.jpg"/>    <meta name="viewport" content="width=device-width">

    <meta name="SKYPE_TOOLBAR" content="SKYPE_TOOLBAR_PARSER_COMPATIBLE" />

	
	<script src="/js/jquery-3.2.1.min.js" defer="defer"></script>
	<script src="/js/jquery.formstyler.min.js" defer="defer"></script>
	<script src="/js/jquery.cookie.js" defer="defer"></script>
	<script src="/js/jquery.fancybox.pack.js" defer="defer"></script>
	<script src="/js/jquery-ui.min.js" defer="defer"></script>
	<script src="/js/jquery.mCustomScrollbar.concat.min.js" defer="defer"></script>
	<script src="/js/modernizr.js" defer="defer"></script>
	<script src="/js/inputmask.min.js" defer="defer"></script>
	<script src="/js/select2.js" defer="defer"></script>
	<script src="/js/main.min.js?v=2.10" defer="defer"></script>
    
	<script src="/js/objects.js"></script>

	<!--[if lte IE 9]><script src="http://html5shiv.googlecode.com/svn/trunk/html5.js"></script><![endif]-->
	<script>
  (function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
  (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
  m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
  })(window,document,'script','https://www.google-analytics.com/analytics.js','ga');

  ga('create', 'UA-83616909-1', 'auto');
  ga('send', 'pageview');

</script>
<!-- Hotjar Tracking Code for https://asbam.com.ua/ -->
<script>
    (function(h,o,t,j,a,r){
        h.hj=h.hj||function(){(h.hj.q=h.hj.q||[]).push(arguments)};
        h._hjSettings={hjid:1661137,hjsv:6};
        a=o.getElementsByTagName('head')[0];
        r=o.createElement('script');r.async=1;
        r.src=t+h._hjSettings.hjid+j+h._hjSettings.hjsv;
        a.appendChild(r);
    })(window,document,'https://static.hotjar.com/c/hotjar-','.js?sv=');
</script>
</head>

<body class="inner">
	<div class="scroll-wrapper search-results-wrapper">
	<header>
		<div class="header-wrapper">
    <div class="toast maintenance hide maintenance-header" role="alert" aria-live="assertive" aria-atomic="true">
    <div class="toast-header">
        <div class="mr-auto"></div>
        <div class="close-button">
            <button type="button" class="ml-2 mb-1 close" data-dismiss="toast" aria-label="Close">
                <img src="/img/close_button.svg">
            </button>
        </div>
    </div>
</div>	<div class="inner-wrapper clearfix">
        <div class="first-line clearfix">
            <div class="logo-item"><a href="/" class="logo"></a></div>
    		<div class="links-wrapper"><a href="#" id="btn-auth"><i class="icon icon-user"></i>власний кабінет</a></div>
                		    <div class="phone-wrapper">
                    <div class="phone-text">Довідка та резервування <span>(8:00 - 20:00):</span></div>
                    <div class="phone-link"><a class="tel-link" href="tel:067 011 22 02">+380 (67) 011 22 02</a></div>
                </div>
                    </div>
                    <div class="second-line clearfix">
                                    <div class="header-item">
                        <a href="#" class="btn-link link-map btn-sm" id="btn-city"><i class="icon icon-marker"></i>ЗМІНИТИ АПТЕКУ</a>
                    </div>
                    <div class="header-item">
                        <p>м. Львів, вул. Городоцька, буд. 82</p>
                    </div>
                                            <div class="header-item">
                            <p><a href="https://goo.gl/mEU5TF" target="_blank" class="link-external-map"><i class="icon icon-map"></i>Дивитись на карті</a></p>
                        </div>
                                        <div class="header-item">
                        <p><a href="#" class="link-timetable" id="btn-timetable"><i class="icon icon-timetable"></i>Години роботи</a></p>
                    </div>
                            </div>
        	</div>
</div>
<div class="search-wrapper">
	<div class="inner-wrapper clearfix">
		<div class="inner-form"><form method="get" accept-charset="utf-8" class="form" id="search-form" action="/search"><div class="field">
	<div class="field-input-holder">
		<input type="text" name="query" class="form-input" placeholder="введіть назву препарату..." id="query" value="Аспірин"/><input type="hidden" name="ext_id" id="ext_id"/>	</div>
			<div class="btn-holder"><button type="submit"><i class="icon icon-search"></i></button></div>
	</div>
</form>
</div>
		<div class="cart-btn-wrapper"><div class="cart-popup-wrapper"><div class="link-holder"><a href="/checkout" class="btn-link btn-big cart-qty-wrapper inactive"><i class="icon icon-cart"></i>КОШИК<span class="cart-qty-holder hidden"> (<span class="cart-qty">0</span>)</span></a>            </div>
            <div class="cart-dropdown">
                <h2><i class="icon icon-cart-red"></i>Товарів в кошику (<span class="cart-qty">0</span>)</h2>
                <div class="cart-wrapper">
                    <table cellspacing="0">
                        <thead>
                            <tr>
                                <td class="a-left col1">Назва товару / Виробник</td>
                                <td class="col6">Кількість</td>
                                <td class="col6 a-left">Вартість</td>
                            </tr>
                        </thead>
                    </table>
                    <div class="cart-body-wrapper">
                        <table cellspacing="0">
                            <tbody id="popup-cart-tbody">
                                                            </tbody>
                        </table>
                    </div>
                    <table cellspacing="0">
                        <tfoot>
                            <tr>
                                <td colspan="2">
                                    <p class="item-title">До сплати:</p>
                                </td>
                                <td class="a-left">
                                    <p class="item-price">
                                        <strong class="cart-total">
                                            0,00&nbsp;грн.                                        </strong>
                                    </p>
                                </td>
                            </tr>
                        </tfoot>
                    </table>
                    <a href="/checkout" class="btn-link btn-md">Оформити замовлення</a>               </div>
            </div>
            </div></div>
	</div>
</div>
    <div id="popup-timetable" style="display:none;">
	<div class="timetable-wrapper">
		<h2>
			<i class="icon icon-timetable"></i>Години роботи
		</h2>
		<div class="timetable-content">
			<p>Понеділок – П’ятниця з <strong>7<sup>45</sup></strong> до <strong>21<sup>15</sup></strong></p>
<p>Субота з <strong>7<sup>45</sup></strong> до <strong>20<sup>15</sup></strong></p>
<p>Неділя з <strong>8<sup>45</sup></strong> до <strong>20<sup>15</sup></strong></p>
		</div>
	</div>
</div>
		<div class="thead-wrapper">
			<div class="inner-wrapper">
				<table cellspacing="0">
					<tr>
						<td class="a-left col1">Назва товару / Виробник</td>
						<td class="col2">Інструкція</td>
						<td class="col3">Відпуск за рецептом</td>
						<td class="col4">Ціна за 1</td>
						<td class="col5">Наявність</td>
						<td class="col6">Кількість на складі</td>
						<td class="col7">&nbsp;</td>
					</tr>
				</table>
			</div>
		</div>
	</header>
	<div class="results-scrollable-wrapper inner-wrapper">
		<div class="content-wrapper">
			<div class="results-wrapper">
									<table cellspacing="0">
													<tr>
								<td class="col1">
									<p class="item-title"><span class="highlight">Аспірин</span> С розч. табл. N10</p>
									<p class="item-brand">Байєр Німеччина</p>
																												<p class="item-similar"><a href="#" data-id="480"><i class="icon-arrow-down"></i>дивитись аналоги товару</a></p>
																	</td>
								<td class="col2"><a href="/instructions/7787/UA43980101_3488.pdf" target="_blank" title="Інструкція"><i class="icon icon-info"></i></a></td>
								<td class="col3">
																	</td>
								<td class="col4">
									<p class="item-price">95,50&nbsp;грн.</p>
								</td>
								<td class="col5">
									<i class="icon-status" title="Є в наявності"></i>								</td>
								<td class="col6">
									<p class="item-qty">5</p>
								</td>
								<td class="col7">
									<a href="#" class="btn-link btn-add-to-cart" 
										data-limit="0" 
										data-title="Аспірин С розч. табл. N10" 
										data-id="480"
									>
										Замовити									</a>
								</td>
							</tr>
															<tbody class="analogue">
																																																	<tr>
												<td class="col1">
													<div class="collapse-box"></div>
													<p class="item-title"><a href="/photos/16838/11730.jpg" target="_blank">Упсарин УПСА+С табл. розч. №10</a></p>
													<p class="item-brand">БМС Франція</p>
												</td>
												<td class="col2"><a href="/instructions/16838/UA75980101_A3DA.pdf" target="_blank" title="Інструкція"><i class="icon icon-info"></i></a></td>
												<td class="col3">
																									</td>
												<td class="col4">
													<p class="item-price">65,99&nbsp;грн.</p>
												</td>
												<td class="col5">
													<p class="item-status">пiд<br>замовлення</p>												</td>
												<td class="col6">
													<p class="item-qty">0</p>
												</td>
												<td class="col7">
													<a href="#" class="btn-link btn-add-to-cart" 
														data-title="Упсарин УПСА+С табл. розч. №10" 
														data-id="11730"
														data-limit="0"
													>
														Замовити													</a>
												</td>
											</tr>
																											</tbody>
																				<tr>
								<td class="col1">
									<p class="item-title"><a href="/photos/10517/27642.jpg" target="_blank"><span class="highlight">Аспірин</span> кардіо табл. п/о 100мг №28</a></p>
									<p class="item-brand">Байєр Німеччина</p>
																												<p class="item-similar"><a href="#" data-id="27642"><i class="icon-arrow-down"></i>дивитись аналоги товару</a></p>
																	</td>
								<td class="col2"><a href="/instructions/10517/UA78020101_7182.pdf" target="_blank" title="Інструкція"><i class="icon icon-info"></i></a></td>
								<td class="col3">
																	</td>
								<td class="col4">
									<p class="item-price">70,50&nbsp;грн.</p>
								</td>
								<td class="col5">
									<i class="icon-status" title="Є в наявності"></i>								</td>
								<td class="col6">
									<p class="item-qty">9</p>
								</td>
								<td class="col7">
									<a href="#" class="btn-link btn-add-to-cart" 
										data-limit="0" 
										data-title="Аспірин кардіо табл. п/о 100мг №28" 
										data-id="27642"
									>
										Замовити									</a>
								</td>
							</tr>
															<tbody class="analogue">
																														<tr>
												<td class="col1">
													<div class="collapse-box"></div>
													<p class="item-title">Асафен табл. 80мг №90</p>
													<p class="item-brand">Фармасайнс Канада</p>
												</td>
												<td class="col2"><a href="/instructions/8132/UA79730101_8819.pdf" target="_blank" title="Інструкція"><i class="icon icon-info"></i></a></td>
												<td class="col3">
																									</td>
												<td class="col4">
													<p class="item-price">114,50&nbsp;грн.</p>
												</td>
												<td class="col5">
													<i class="icon-status"></i>												</td>
												<td class="col6">
													<p class="item-qty">2</p>
												</td>
												<td class="col7">
													<a href="#" class="btn-link btn-add-to-cart" 
														data-title="Асафен табл. 80мг №90" 
														data-id="15718"
														data-limit="0"
													>
														Замовити													</a>
												</td>
											</tr>
																																								<tr>
												<td class="col1">
													<div class="collapse-box"></div>
													<p class="item-title">Тромбо АСС табл. 100мг №30</p>
													<p class="item-brand">Джі еЛ Фарма Австрія</p>
												</td>
												<td class="col2"><a href="/instructions/9535/UA53730101_723E.pdf" target="_blank" title="Інструкція"><i class="icon icon-info"></i></a></td>
												<td class="col3">
																									</td>
												<td class="col4">
													<p class="item-price">69,50&nbsp;грн.</p>
												</td>
												<td class="col5">
													<p class="item-status">пiд<br>замовлення</p>												</td>
												<td class="col6">
													<p class="item-qty">0</p>
												</td>
												<td class="col7">
													<a href="#" class="btn-link btn-add-to-cart" 
														data-title="Тромбо АСС табл. 100мг №30" 
														data-id="23418"
														data-limit="0"
													>
														Замовити													</a>
												</td>
											</tr>
																																								<tr>
												<td class="col1">
													<div class="collapse-box"></div>
													<p class="item-title">Тромбо АСС табл. 75мг №30</p>
													<p class="item-brand">Джі еЛ Фарма Австрія</p>
												</td>
												<td class="col2"><a href="/instructions/9537/UA53730103_0C91.pdf" target="_blank" title="Інструкція"><i class="icon icon-info"></i></a></td>
												<td class="col3">
																									</td>
												<td class="col4">
													<p class="item-price">59,99&nbsp;грн.</p>
												</td>
												<td class="col5">
													<p class="item-status">пiд<br>замовлення</p>												</td>
												<td class="col6">
													<p class="item-qty">0</p>
												</td>
												<td class="col7">
													<a href="#" class="btn-link btn-add-to-cart" 
														data-title="Тромбо АСС табл. 75мг №30" 
														data-id="23420"
														data-limit="0"
													>
														Замовити													</a>
												</td>
											</tr>
																																								<tr>
												<td class="col1">
													<div class="collapse-box"></div>
													<p class="item-title">Ацекор Кардіо табл. 100мг №50</p>
													<p class="item-brand">Мікрохім Україна Рубіжне</p>
												</td>
												<td class="col2"><a href="/instructions/9748/UA96280101_00DB.pdf" target="_blank" title="Інструкція"><i class="icon icon-info"></i></a></td>
												<td class="col3">
																									</td>
												<td class="col4">
													<p class="item-price">68,50&nbsp;грн.</p>
												</td>
												<td class="col5">
													<i class="icon-status"></i>												</td>
												<td class="col6">
													<p class="item-qty">1</p>
												</td>
												<td class="col7">
													<a href="#" class="btn-link btn-add-to-cart" 
														data-title="Ацекор Кардіо табл. 100мг №50" 
														data-id="26845"
														data-limit="0"
													>
														Замовити													</a>
												</td>
											</tr>
																																								<tr>
												<td class="col1">
													<div class="collapse-box"></div>
													<p class="item-title">Лоспірин табл. 75мг №30</p>
													<p class="item-brand">Кусум Індія</p>
												</td>
												<td class="col2"><a href="/instructions/10119/UA92020101_CECE.pdf" target="_blank" title="Інструкція"><i class="icon icon-info"></i></a></td>
												<td class="col3">
																									</td>
												<td class="col4">
													<p class="item-price">34,20&nbsp;грн.</p>
												</td>
												<td class="col5">
													<i class="icon-status"></i>												</td>
												<td class="col6">
													<p class="item-qty">1</p>
												</td>
												<td class="col7">
													<a href="#" class="btn-link btn-add-to-cart" 
														data-title="Лоспірин табл. 75мг №30" 
														data-id="28690"
														data-limit="0"
													>
														Замовити													</a>
												</td>
											</tr>
																																																											<tr>
												<td class="col1">
													<div class="collapse-box"></div>
													<p class="item-title"><a href="/photos/10519/27475.jpg" target="_blank"><span class="highlight">Аспірин</span> кардіо табл. п/о 300мг №28</a></p>
													<p class="item-brand">Байєр Німеччина</p>
												</td>
												<td class="col2"><a href="/instructions/10519/UA78020102_9726.pdf" target="_blank" title="Інструкція"><i class="icon icon-info"></i></a></td>
												<td class="col3">
																									</td>
												<td class="col4">
													<p class="item-price">102,99&nbsp;грн.</p>
												</td>
												<td class="col5">
													<p class="item-status">пiд<br>замовлення</p>												</td>
												<td class="col6">
													<p class="item-qty">0</p>
												</td>
												<td class="col7">
													<a href="#" class="btn-link btn-add-to-cart" 
														data-title="Аспірин кардіо табл. п/о 300мг №28" 
														data-id="27475"
														data-limit="0"
													>
														Замовити													</a>
												</td>
											</tr>
																																								<tr>
												<td class="col1">
													<div class="collapse-box"></div>
													<p class="item-title">Тромболік Кардіо табл. 100мг №20</p>
													<p class="item-brand">Технолог Україна</p>
												</td>
												<td class="col2"><a href="/instructions/11327/UA106970101_07EC.pdf" target="_blank" title="Інструкція"><i class="icon icon-info"></i></a></td>
												<td class="col3">
																									</td>
												<td class="col4">
													<p class="item-price">41,31&nbsp;грн.</p>
												</td>
												<td class="col5">
													<i class="icon-status"></i>												</td>
												<td class="col6">
													<p class="item-qty">2</p>
												</td>
												<td class="col7">
													<a href="#" class="btn-link btn-add-to-cart" 
														data-title="Тромболік Кардіо табл. 100мг №20" 
														data-id="37505"
														data-limit="0"
													>
														Замовити													</a>
												</td>
											</tr>
																																								<tr>
												<td class="col1">
													<div class="collapse-box"></div>
													<p class="item-title"><a href="/photos/11807/43392.jpg" target="_blank">Лоспірин табл. 75мг №120</a></p>
													<p class="item-brand">Кусум Фарм Україна Суми</p>
												</td>
												<td class="col2"><a href="/instructions/11807/43392.pdf" target="_blank" title="Інструкція"><i class="icon icon-info"></i></a></td>
												<td class="col3">
																									</td>
												<td class="col4">
													<p class="item-price">89,50&nbsp;грн.</p>
												</td>
												<td class="col5">
													<i class="icon-status"></i>												</td>
												<td class="col6">
													<p class="item-qty">2</p>
												</td>
												<td class="col7">
													<a href="#" class="btn-link btn-add-to-cart" 
														data-title="Лоспірин табл. 75мг №120" 
														data-id="43392"
														data-limit="0"
													>
														Замовити													</a>
												</td>
											</tr>
																																								<tr>
												<td class="col1">
													<div class="collapse-box"></div>
													<p class="item-title">Акард табл. 75мг №50</p>
													<p class="item-brand">Польфарма Польша</p>
												</td>
												<td class="col2"><a href="/instructions/11930/45990.pdf" target="_blank" title="Інструкція"><i class="icon icon-info"></i></a></td>
												<td class="col3">
																									</td>
												<td class="col4">
													<p class="item-price">65,50&nbsp;грн.</p>
												</td>
												<td class="col5">
													<i class="icon-status"></i>												</td>
												<td class="col6">
													<p class="item-qty">3</p>
												</td>
												<td class="col7">
													<a href="#" class="btn-link btn-add-to-cart" 
														data-title="Акард табл. 75мг №50" 
														data-id="45990"
														data-limit="0"
													>
														Замовити													</a>
												</td>
											</tr>
																																								<tr>
												<td class="col1">
													<div class="collapse-box"></div>
													<p class="item-title">Акард табл. 150мг №50</p>
													<p class="item-brand">Польфарма Польша</p>
												</td>
												<td class="col2"><a href="/instructions/11931/45991.pdf" target="_blank" title="Інструкція"><i class="icon icon-info"></i></a></td>
												<td class="col3">
																									</td>
												<td class="col4">
													<p class="item-price">81,99&nbsp;грн.</p>
												</td>
												<td class="col5">
													<p class="item-status">пiд<br>замовлення</p>												</td>
												<td class="col6">
													<p class="item-qty">0</p>
												</td>
												<td class="col7">
													<a href="#" class="btn-link btn-add-to-cart" 
														data-title="Акард табл. 150мг №50" 
														data-id="45991"
														data-limit="0"
													>
														Замовити													</a>
												</td>
											</tr>
																																								<tr>
												<td class="col1">
													<div class="collapse-box"></div>
													<p class="item-title">Кардісейв табл. п/о 75мг №50</p>
													<p class="item-brand">Фармак Україна</p>
												</td>
												<td class="col2"><a href="/instructions/11951/46513.pdf" target="_blank" title="Інструкція"><i class="icon icon-info"></i></a></td>
												<td class="col3">
																									</td>
												<td class="col4">
													<p class="item-price">21,90&nbsp;грн.</p>
												</td>
												<td class="col5">
													<p class="item-status">пiд<br>замовлення</p>												</td>
												<td class="col6">
													<p class="item-qty">0</p>
												</td>
												<td class="col7">
													<a href="#" class="btn-link btn-add-to-cart" 
														data-title="Кардісейв табл. п/о 75мг №50" 
														data-id="46513"
														data-limit="0"
													>
														Замовити													</a>
												</td>
											</tr>
																																								<tr>
												<td class="col1">
													<div class="collapse-box"></div>
													<p class="item-title">Ацекор Кардіо табл. 100мг №100</p>
													<p class="item-brand">Мікрохім Україна Рубіжне</p>
												</td>
												<td class="col2"><a href="/instructions/29168/46996.pdf" target="_blank" title="Інструкція"><i class="icon icon-info"></i></a></td>
												<td class="col3">
																									</td>
												<td class="col4">
													<p class="item-price">97,50&nbsp;грн.</p>
												</td>
												<td class="col5">
													<i class="icon-status"></i>												</td>
												<td class="col6">
													<p class="item-qty">2</p>
												</td>
												<td class="col7">
													<a href="#" class="btn-link btn-add-to-cart" 
														data-title="Ацекор Кардіо табл. 100мг №100" 
														data-id="46996"
														data-limit="0"
													>
														Замовити													</a>
												</td>
											</tr>
																																								<tr>
												<td class="col1">
													<div class="collapse-box"></div>
													<p class="item-title">Аспікард кардіо табл. п/о 100мг №20</p>
													<p class="item-brand">Вертекс Україна</p>
												</td>
												<td class="col2"></td>
												<td class="col3">
																											<i class="icon icon-card"></i>
																									</td>
												<td class="col4">
													<p class="item-price">27,80&nbsp;грн.</p>
												</td>
												<td class="col5">
													<p class="item-status">пiд<br>замовлення</p>												</td>
												<td class="col6">
													<p class="item-qty">0</p>
												</td>
												<td class="col7">
													<a href="#" class="btn-link btn-add-to-cart" 
														data-title="Аспікард кардіо табл. п/о 100мг №20" 
														data-id="57138"
														data-limit="0"
													>
														Замовити													</a>
												</td>
											</tr>
																											</tbody>
																				<tr>
								<td class="col1">
									<p class="item-title"><a href="/photos/10519/27475.jpg" target="_blank"><span class="highlight">Аспірин</span> кардіо табл. п/о 300мг №28</a></p>
									<p class="item-brand">Байєр Німеччина</p>
																												<p class="item-similar"><a href="#" data-id="27475"><i class="icon-arrow-down"></i>дивитись аналоги товару</a></p>
																	</td>
								<td class="col2"><a href="/instructions/10519/UA78020102_9726.pdf" target="_blank" title="Інструкція"><i class="icon icon-info"></i></a></td>
								<td class="col3">
																	</td>
								<td class="col4">
									<p class="item-price">102,99&nbsp;грн.</p>
								</td>
								<td class="col5">
									<p class="item-status">пiд<br>замовлення</p>								</td>
								<td class="col6">
									<p class="item-qty">0</p>
								</td>
								<td class="col7">
									<a href="#" class="btn-link btn-add-to-cart" 
										data-limit="0" 
										data-title="Аспірин кардіо табл. п/о 300мг №28" 
										data-id="27475"
									>
										Замовити									</a>
								</td>
							</tr>
															<tbody class="analogue">
																														<tr>
												<td class="col1">
													<div class="collapse-box"></div>
													<p class="item-title">Асафен табл. 80мг №90</p>
													<p class="item-brand">Фармасайнс Канада</p>
												</td>
												<td class="col2"><a href="/instructions/8132/UA79730101_8819.pdf" target="_blank" title="Інструкція"><i class="icon icon-info"></i></a></td>
												<td class="col3">
																									</td>
												<td class="col4">
													<p class="item-price">114,50&nbsp;грн.</p>
												</td>
												<td class="col5">
													<i class="icon-status"></i>												</td>
												<td class="col6">
													<p class="item-qty">2</p>
												</td>
												<td class="col7">
													<a href="#" class="btn-link btn-add-to-cart" 
														data-title="Асафен табл. 80мг №90" 
														data-id="15718"
														data-limit="0"
													>
														Замовити													</a>
												</td>
											</tr>
																																								<tr>
												<td class="col1">
													<div class="collapse-box"></div>
													<p class="item-title">Тромбо АСС табл. 100мг №30</p>
													<p class="item-brand">Джі еЛ Фарма Австрія</p>
												</td>
												<td class="col2"><a href="/instructions/9535/UA53730101_723E.pdf" target="_blank" title="Інструкція"><i class="icon icon-info"></i></a></td>
												<td class="col3">
																									</td>
												<td class="col4">
													<p class="item-price">69,50&nbsp;грн.</p>
												</td>
												<td class="col5">
													<p class="item-status">пiд<br>замовлення</p>												</td>
												<td class="col6">
													<p class="item-qty">0</p>
												</td>
												<td class="col7">
													<a href="#" class="btn-link btn-add-to-cart" 
														data-title="Тромбо АСС табл. 100мг №30" 
														data-id="23418"
														data-limit="0"
													>
														Замовити													</a>
												</td>
											</tr>
																																								<tr>
												<td class="col1">
													<div class="collapse-box"></div>
													<p class="item-title">Тромбо АСС табл. 75мг №30</p>
													<p class="item-brand">Джі еЛ Фарма Австрія</p>
												</td>
												<td class="col2"><a href="/instructions/9537/UA53730103_0C91.pdf" target="_blank" title="Інструкція"><i class="icon icon-info"></i></a></td>
												<td class="col3">
																									</td>
												<td class="col4">
													<p class="item-price">59,99&nbsp;грн.</p>
												</td>
												<td class="col5">
													<p class="item-status">пiд<br>замовлення</p>												</td>
												<td class="col6">
													<p class="item-qty">0</p>
												</td>
												<td class="col7">
													<a href="#" class="btn-link btn-add-to-cart" 
														data-title="Тромбо АСС табл. 75мг №30" 
														data-id="23420"
														data-limit="0"
													>
														Замовити													</a>
												</td>
											</tr>
																																								<tr>
												<td class="col1">
													<div class="collapse-box"></div>
													<p class="item-title">Ацекор Кардіо табл. 100мг №50</p>
													<p class="item-brand">Мікрохім Україна Рубіжне</p>
												</td>
												<td class="col2"><a href="/instructions/9748/UA96280101_00DB.pdf" target="_blank" title="Інструкція"><i class="icon icon-info"></i></a></td>
												<td class="col3">
																									</td>
												<td class="col4">
													<p class="item-price">68,50&nbsp;грн.</p>
												</td>
												<td class="col5">
													<i class="icon-status"></i>												</td>
												<td class="col6">
													<p class="item-qty">1</p>
												</td>
												<td class="col7">
													<a href="#" class="btn-link btn-add-to-cart" 
														data-title="Ацекор Кардіо табл. 100мг №50" 
														data-id="26845"
														data-limit="0"
													>
														Замовити													</a>
												</td>
											</tr>
																																								<tr>
												<td class="col1">
													<div class="collapse-box"></div>
													<p class="item-title">Лоспірин табл. 75мг №30</p>
													<p class="item-brand">Кусум Індія</p>
												</td>
												<td class="col2"><a href="/instructions/10119/UA92020101_CECE.pdf" target="_blank" title="Інструкція"><i class="icon icon-info"></i></a></td>
												<td class="col3">
																									</td>
												<td class="col4">
													<p class="item-price">34,20&nbsp;грн.</p>
												</td>
												<td class="col5">
													<i class="icon-status"></i>												</td>
												<td class="col6">
													<p class="item-qty">1</p>
												</td>
												<td class="col7">
													<a href="#" class="btn-link btn-add-to-cart" 
														data-title="Лоспірин табл. 75мг №30" 
														data-id="28690"
														data-limit="0"
													>
														Замовити													</a>
												</td>
											</tr>
																																								<tr>
												<td class="col1">
													<div class="collapse-box"></div>
													<p class="item-title"><a href="/photos/10517/27642.jpg" target="_blank"><span class="highlight">Аспірин</span> кардіо табл. п/о 100мг №28</a></p>
													<p class="item-brand">Байєр Німеччина</p>
												</td>
												<td class="col2"><a href="/instructions/10517/UA78020101_7182.pdf" target="_blank" title="Інструкція"><i class="icon icon-info"></i></a></td>
												<td class="col3">
																									</td>
												<td class="col4">
													<p class="item-price">70,50&nbsp;грн.</p>
												</td>
												<td class="col5">
													<i class="icon-status"></i>												</td>
												<td class="col6">
													<p class="item-qty">9</p>
												</td>
												<td class="col7">
													<a href="#" class="btn-link btn-add-to-cart" 
														data-title="Аспірин кардіо табл. п/о 100мг №28" 
														data-id="27642"
														data-limit="0"
													>
														Замовити													</a>
												</td>
											</tr>
																																																											<tr>
												<td class="col1">
													<div class="collapse-box"></div>
													<p class="item-title">Тромболік Кардіо табл. 100мг №20</p>
													<p class="item-brand">Технолог Україна</p>
												</td>
												<td class="col2"><a href="/instructions/11327/UA106970101_07EC.pdf" target="_blank" title="Інструкція"><i class="icon icon-info"></i></a></td>
												<td class="col3">
																									</td>
												<td class="col4">
													<p class="item-price">41,31&nbsp;грн.</p>
												</td>
												<td class="col5">
													<i class="icon-status"></i>												</td>
												<td class="col6">
													<p class="item-qty">2</p>
												</td>
												<td class="col7">
													<a href="#" class="btn-link btn-add-to-cart" 
														data-title="Тромболік Кардіо табл. 100мг №20" 
														data-id="37505"
														data-limit="0"
													>
														Замовити													</a>
												</td>
											</tr>
																																								<tr>
												<td class="col1">
													<div class="collapse-box"></div>
													<p class="item-title"><a href="/photos/11807/43392.jpg" target="_blank">Лоспірин табл. 75мг №120</a></p>
													<p class="item-brand">Кусум Фарм Україна Суми</p>
												</td>
												<td class="col2"><a href="/instructions/11807/43392.pdf" target="_blank" title="Інструкція"><i class="icon icon-info"></i></a></td>
												<td class="col3">
																									</td>
												<td class="col4">
													<p class="item-price">89,50&nbsp;грн.</p>
												</td>
												<td class="col5">
													<i class="icon-status"></i>												</td>
												<td class="col6">
													<p class="item-qty">2</p>
												</td>
												<td class="col7">
													<a href="#" class="btn-link btn-add-to-cart" 
														data-title="Лоспірин табл. 75мг №120" 
														data-id="43392"
														data-limit="0"
													>
														Замовити													</a>
												</td>
											</tr>
																																								<tr>
												<td class="col1">
													<div class="collapse-box"></div>
													<p class="item-title">Акард табл. 75мг №50</p>
													<p class="item-brand">Польфарма Польша</p>
												</td>
												<td class="col2"><a href="/instructions/11930/45990.pdf" target="_blank" title="Інструкція"><i class="icon icon-info"></i></a></td>
												<td class="col3">
																									</td>
												<td class="col4">
													<p class="item-price">65,50&nbsp;грн.</p>
												</td>
												<td class="col5">
													<i class="icon-status"></i>												</td>
												<td class="col6">
													<p class="item-qty">3</p>
												</td>
												<td class="col7">
													<a href="#" class="btn-link btn-add-to-cart" 
														data-title="Акард табл. 75мг №50" 
														data-id="45990"
														data-limit="0"
													>
														Замовити													</a>
												</td>
											</tr>
																																								<tr>
												<td class="col1">
													<div class="collapse-box"></div>
													<p class="item-title">Акард табл. 150мг №50</p>
													<p class="item-brand">Польфарма Польша</p>
												</td>
												<td class="col2"><a href="/instructions/11931/45991.pdf" target="_blank" title="Інструкція"><i class="icon icon-info"></i></a></td>
												<td class="col3">
																									</td>
												<td class="col4">
													<p class="item-price">81,99&nbsp;грн.</p>
												</td>
												<td class="col5">
													<p class="item-status">пiд<br>замовлення</p>												</td>
												<td class="col6">
													<p class="item-qty">0</p>
												</td>
												<td class="col7">
													<a href="#" class="btn-link btn-add-to-cart" 
														data-title="Акард табл. 150мг №50" 
														data-id="45991"
														data-limit="0"
													>
														Замовити													</a>
												</td>
											</tr>
																																								<tr>
												<td class="col1">
													<div class="collapse-box"></div>
													<p class="item-title">Кардісейв табл. п/о 75мг №50</p>
													<p class="item-brand">Фармак Україна</p>
												</td>
												<td class="col2"><a href="/instructions/11951/46513.pdf" target="_blank" title="Інструкція"><i class="icon icon-info"></i></a></td>
												<td class="col3">
																									</td>
												<td class="col4">
													<p class="item-price">21,90&nbsp;грн.</p>
												</td>
												<td class="col5">
													<p class="item-status">пiд<br>замовлення</p>												</td>
												<td class="col6">
													<p class="item-qty">0</p>
												</td>
												<td class="col7">
													<a href="#" class="btn-link btn-add-to-cart" 
														data-title="Кардісейв табл. п/о 75мг №50" 
														data-id="46513"
														data-limit="0"
													>
														Замовити													</a>
												</td>
											</tr>
																																								<tr>
												<td class="col1">
													<div class="collapse-box"></div>
													<p class="item-title">Ацекор Кардіо табл. 100мг №100</p>
													<p class="item-brand">Мікрохім Україна Рубіжне</p>
												</td>
												<td class="col2"><a href="/instructions/29168/46996.pdf" target="_blank" title="Інструкція"><i class="icon icon-info"></i></a></td>
												<td class="col3">
																									</td>
												<td class="col4">
													<p class="item-price">97,50&nbsp;грн.</p>
												</td>
												<td class="col5">
													<i class="icon-status"></i>												</td>
												<td class="col6">
													<p class="item-qty">2</p>
												</td>
												<td class="col7">
													<a href="#" class="btn-link btn-add-to-cart" 
														data-title="Ацекор Кардіо табл. 100мг №100" 
														data-id="46996"
														data-limit="0"
													>
														Замовити													</a>
												</td>
											</tr>
																																								<tr>
												<td class="col1">
													<div class="collapse-box"></div>
													<p class="item-title">Аспікард кардіо табл. п/о 100мг №20</p>
													<p class="item-brand">Вертекс Україна</p>
												</td>
												<td class="col2"></td>
												<td class="col3">
																											<i class="icon icon-card"></i>
																									</td>
												<td class="col4">
													<p class="item-price">27,80&nbsp;грн.</p>
												</td>
												<td class="col5">
													<p class="item-status">пiд<br>замовлення</p>												</td>
												<td class="col6">
													<p class="item-qty">0</p>
												</td>
												<td class="col7">
													<a href="#" class="btn-link btn-add-to-cart" 
														data-title="Аспікард кардіо табл. п/о 100мг №20" 
														data-id="57138"
														data-limit="0"
													>
														Замовити													</a>
												</td>
											</tr>
																											</tbody>
																		</table>
							</div>
		</div>
	</div>
</div>
<div id="popup-warehouse" style="display:none;">
    <div class="warehouse-box city-box">
        <div class="selected-warehouse">
                            <i class="icon icon-placemark"></i> Змінити адресу аптеки
                    </div>
        <div class="selected-city">
            <div id="selected-city" class="selected-city-title"></div>
            <a href="#" class="btn-link btn-sm" id="btn-city-popup"><i class="icon icon-marker"></i>ЗМІНИТИ МІСТО</a>
        </div>
        <div class="field field-select">
            <select class="form-select" data-placeholder="Виберіть адресу аптеки" id="warehouse">
                <option value="" selected>Виберіть адресу аптеки</option>
            </select>
        </div>
        <p class="form-hint">Ваше замовлення Ви зможете отримати в аптеці БАМ за вказаною Вами адресою</p>

        
        <p class="map-links-block clearfix" id="map-links-block">
            <a href="#" id="warehouse-link" target="_blank" class="warehouse-link-map"><i class="icon icon-map"></i>Дивитись на карті</a>
            <a href="https://www.google.com/maps/d/u/0/viewer?mid=1nx76DbEFz2y6Mg0rMKhv5J_j7fg" target="_blank" class="btn-link btn-md link-map"><i class="icon icon-marker"></i>ВСІ АПТЕКИ НА КАРТІ</a>
        </p>
        <div class="select-warehouse-selector">
            <a href="#" class="btn-link btn-warehouse-select btn-disabled btn-md" id="btn-warehouse-select">ПІДТВЕРДИТИ АДРЕСУ АПТЕКИ</a>
        </div>
    </div>
</div>
<div id="popup-city" style="display:none;">
    <div class="warehouse-box city-box">
        <div class="selected-warehouse">
                            <i class="icon icon-placemark"></i> Змінити місто
                    </div>
        <div class="field field-select">
            <select class="form-select" data-placeholder="Виберіть місто" id="city">
                <option value="" selected>Виберіть місто</option>
                                    <option value="1896">Дніпро&nbsp;</option>
                                    <option value="2054" selected>Львів&nbsp;</option>
                                    <option value="2531">Олександрія (м.Кіровогр.обл.райц)&nbsp;</option>
                                    <option value="1779">Біла Церква&nbsp;</option>
                                    <option value="1844">Вінниця&nbsp;</option>
                                    <option value="1855">Волочиськ&nbsp;</option>
                                    <option value="1909">Дубно&nbsp;</option>
                                    <option value="1920">Житомир&nbsp;</option>
                                    <option value="1924">Запоріжжя&nbsp;</option>
                                    <option value="1946">Івано-Франківськ&nbsp;</option>
                                    <option value="1963">Калуш&nbsp;</option>
                                    <option value="1976">Київ&nbsp;</option>
                                    <option value="2023">Кременець&nbsp;</option>
                                    <option value="2027">Кривий Ріг&nbsp;</option>
                                    <option value="1978">Кропивницький&nbsp;</option>
                                    <option value="2030">Крижопіль&nbsp;</option>
                                    <option value="2052">Луцьк&nbsp;</option>
                                    <option value="2070">Маріуполь&nbsp;</option>
                                    <option value="2075">Мелітополь&nbsp;</option>
                                    <option value="2088">Мукачево&nbsp;</option>
                                    <option value="2090">Надвірна&nbsp;</option>
                                    <option value="2111">Нововолинськ&nbsp;</option>
                                    <option value="2121">Новояворівськ&nbsp;</option>
                                    <option value="2896">Новий Розділ&nbsp;</option>
                                    <option value="1609">Павлоград&nbsp;</option>
                                    <option value="1615">Переяслав&nbsp;</option>
                                    <option value="1625">Полтава&nbsp;</option>
                                    <option value="1638">Рені&nbsp;</option>
                                    <option value="1642">Рівне&nbsp;</option>
                                    <option value="1654">Свалява&nbsp;</option>
                                    <option value="1655">Сватове&nbsp;</option>
                                    <option value="1666">Славутич&nbsp;</option>
                                    <option value="1687">Суми&nbsp;</option>
                                    <option value="1698">Тернопіль&nbsp;</option>
                                    <option value="1713">Умань&nbsp;</option>
                                    <option value="1716">Харків&nbsp;</option>
                                    <option value="1718">Хмельницький&nbsp;</option>
                                    <option value="1727">Черкаси&nbsp;</option>
                                    <option value="1728">Чернігів&nbsp;</option>
                                    <option value="1729">Чернівці&nbsp;</option>
                <!--                <option value="0"--><!-- selected--><!--Інше місто</option>-->
            </select>
        </div>

                            <div class="popup-hint">
                В іншій аптеці ціна і наявність товарів можуть відрізнятися. Перевірте, будь ласка, корзину.
            </div>
        
        <!--        <p class="form-hint">Якщо Ви не знайшли свого міста серед переліку, оберіть<br><strong>ІНШЕ МІСТО</strong> і ви зможете замовити ліки з доставкою на вказану<br>Вами адресу або склад Нової Пошти.</p>-->
        <a href="#" class="btn-link btn-city-select btn-disabled btn-md" id="btn-city-select">Підтвердити</a>
        <div id="btn-warehouse"></div>
    </div>
</div>
<div class="hidden" id="cant-add-to-cart"></div>
<div id="popup-cant-add-to-cart" style="display:none;">
    <div class="added-to-cart-wrapper cant-add-wrapper">
        <h2>
            <i class="icon icon-cart-red"></i>Даний лікарський засіб має обмежені умови відпуску
        </h2>
        <div class="cant-add-to-cart-content">
            <p>Його можна придбати лише на БАМі у вашому місті</p>
            <p>деталі у провізорів або ж за телефоном довідки</p>
            <p>067 011 22 02</p>
        </div>
        <p class="btn-block"><a href="#" class="btn-link popup-content-close">Продовжити покупки</a></p>
    </div>
</div>
<div class="hidden" id="btn-added-to-cart"></div>
<div id="popup-added-to-cart" style="display:none;">
	<div class="added-to-cart-wrapper">
		<h2>
			<i class="icon icon-cart-red"></i>Товар додано у кошик
		</h2>
        <div class="cart-wrapper">
            <table cellspacing="0">
                <thead>
                    <tr>
                        <td class="a-left col1">Назва товару / Виробник</td>
                        <td class="col2">Ціна за 1</td>
                        <td class="col3">Кількість</td>
                        <td class="col4 a-left">Вартість</td>
                    </tr>
                </thead>
                <tbody id="popup-cart-item-tbody"></tbody>
            </table>
        </div>
		<p class="btn-block"><a href="/checkout" class="btn-link">Оформити замовлення</a><a href="#" class="btn-link popup-content-close">Продовжити покупки</a></p>
	</div>
</div>
<div id="popup-auth" style="display:none;">
	<div class="auth-wrapper" id="auth-block">
		<h2>
			<i class="icon icon-auth"></i><br>
			Вхід в особистий кабінет
		</h2>
		<div class="auth-form">
			<form method="post" accept-charset="utf-8" class="form" id="auth-form" action="/login"><div style="display:none;"><input type="hidden" name="_method" value="POST"/></div>				<div class="field">
					<div class="field-input-holder">
						<input type="tel" name="phone" class="form-input" id="login-phone" placeholder="НОМЕР ТЕЛЕФОНУ" required="required" oninvalid="this.setCustomValidity(&quot;Вкажіть номер телефону&quot;)" oninput="this.setCustomValidity(&quot;&quot;)"/>						<div class="field-error hidden">Телефон або пароль вказано невірно</div>
					</div>
				</div>
				<div class="field">
					<div class="field-input-holder"><input type="password" name="password" class="form-input" placeholder="ПАРОЛЬ" required="required" oninvalid="this.setCustomValidity(&quot;Вкажіть пароль&quot;)" oninput="this.setCustomValidity(&quot;&quot;)"/></div>
				</div>
				<div class="auth-link-wrapper"><a href="#" id="link-remind"><i class="icon icon-key"></i>Забули пароль?</a></div>
				<button type="submit" class="btn">УВІЙТИ</button>
				<div class="auth-link-wrapper"><a href="/register"><i class="icon icon-register"></i>ЗАРЕЄСТРУВАТИСЯ</a></div>
			</form>		</div>
	</div>
	<div class="auth-wrapper hidden" id="remind-block">
		<h2>
			<i class="icon icon-envelope"></i><br>
			Забули пароль?
		</h2>
		<div class="auth-form">
			<form method="post" accept-charset="utf-8" class="form" id="remind-form" action="/remind"><div style="display:none;"><input type="hidden" name="_method" value="POST"/></div>				<div class="field">
					<div class="field-input-holder">
						<input type="tel" name="phone" class="form-input" id="remind-phone" placeholder="НОМЕР ТЕЛЕФОНУ" required="required" oninvalid="this.setCustomValidity(&quot;Вкажіть номер телефону&quot;)" oninput="this.setCustomValidity(&quot;&quot;)"/>						<div class="field-error hidden" id="error-remind"></div>
					</div>
				</div>
				<div class="auth-link-wrapper"><a href="#" id="link-auth"><i class="icon icon-register"></i>Я згадав пароль</a></div>
				<button type="submit" class="btn">Надіслати код</button>
			</form>		</div>
	</div>
	<div class="auth-wrapper hidden" id="password-block">
		<h2>
			<i class="icon icon-envelope"></i><br>
			Ми вислали Вам смс з кодом підтвердження на номер <strong id="sent-phone"></strong>
		</h2>
		<div class="auth-form">
			<form method="post" accept-charset="utf-8" class="form" id="password-form" action="/change-password"><div style="display:none;"><input type="hidden" name="_method" value="POST"/></div>				<input type="hidden" name="phone" id="change-password-phone"/>				<div class="field">
					<div class="field-input-holder">
						<input type="text" name="code" class="form-input" id="remind-code" placeholder="КОД З SMS" required="required" oninvalid="this.setCustomValidity(&quot;Вкажіть код з SMS&quot;)" oninput="this.setCustomValidity(&quot;&quot;)"/>						<div class="field-error hidden" id="error-code"></div>
					</div>
				</div>
				<div class="field">
					<div class="field-input-holder">
						<input type="password" name="password" class="form-input" placeholder="НОВИЙ ПАРОЛЬ" required="required" oninvalid="this.setCustomValidity(&quot;Вкажіть новий пароль&quot;)" oninput="this.setCustomValidity(&quot;&quot;)"/>						<div class="field-error hidden" id="error-password"></div>
					</div>
				</div>
				<div class="field">
					<div class="field-input-holder">
						<input type="password" name="confirm_password" class="form-input" placeholder="НОВИЙ ПАРОЛЬ ПОВТОРНО" required="required" oninvalid="this.setCustomValidity(&quot;Вкажіть новий пароль повторно&quot;)" oninput="this.setCustomValidity(&quot;&quot;)"/>						<div class="field-error hidden" id="error-confirm_password"></div>
					</div>
				</div>
				<div class="auth-link-wrapper"><a href="#" id="link-send-again">Надіслати код ще раз</a></div>
				<button type="submit" class="btn">Змінити пароль</button>
				<div class="auth-link-wrapper"><a href="#" id="link-remind-back"><i class="icon icon-key"></i>Інший номер телефону?</a></div>
			</form>		</div>
	</div>
</div>
	<div id="popup-contract" style="display:none;">
	<div class="terms-wrapper">
		<h2>Публічний договір на&nbsp;замовлення, придбання та&nbsp;доставку Товарів</h2>
		<div class="terms-content contract-content">
            <p class="text-justified"> Цей договір між Фізичною особою-підприємцем Мазуром Андрієм Васильовичем (згідно Договору про передачу прав на&nbsp;користування Веб-сайтом &laquo;https://asbam.com.ua/&raquo;), в&nbsp;подальшому &laquo;ФОП&raquo; та&nbsp;будь-якою особою&nbsp;&mdash; замовником послуг на&nbsp;інтренет-сайті, в&nbsp;подальшому&nbsp;&mdash; &laquo;Замовник&raquo;. Цей Договір є&nbsp;договором доручення на&nbsp;замовлення, придбання та&nbsp;доставку Товарів та&nbsp;визначає основні умови замовлення, придбання та&nbsp;доставки товарів за&nbsp;допомогою інтернет-сайта https://asbam.com.ua/.</p>
            <h3 class="text-no-padding">1. ЗАГАЛЬНІ УМОВИ</h3>
            <p class="text-no-padding">1.1. ФОП оприлюднює цей договір, який є&nbsp;публічним договором&nbsp;&mdash; офертою (пропозицією) на&nbsp;адресу фізичних та&nbsp;юридичних осіб відповідно до&nbsp;ст.633&nbsp;ЦК України.</p>
            <p class="text-no-padding">1.2. Ця&nbsp;публічна оферта (в&nbsp;подальшому&nbsp;&mdash; &laquo;Оферта&raquo;) визначає всі істотні умови договору між ФОП та&nbsp;особою, яка акцептує Оферту.</p>
            <p class="text-no-padding">1.3. Оферта може бути акцептована (прийнята) будь-якою фізичною особою або юридичною особою на&nbsp;території України, за&nbsp;виключенням окупованих територій, яка має намір замовити товар за&nbsp;допомогою інтернет-сайту, інформація про який розміщена на&nbsp;сайті https://asbam.com.ua/.</p>
            <p class="text-no-padding">1.4. Замовник беззаперечно приймає всі умови, які містяться в&nbsp;Оферті в&nbsp;цілому (тобто в&nbsp;повному обсязі та&nbsp;без виключень).</p>
            <p class="text-no-padding">1.5. У&nbsp;випадку прийняття умов цього Договору, фізична або юридична особа, яка здійснює акцепт Оферти, набуває статусу Замовника. Акцептом є&nbsp;факт замовлення товарів на&nbsp;сайті https://asbam.com.ua/ та/або замовлення товарів за&nbsp;телефоном.</p>
            <h3 class="text-no-padding">3. СТАТУС ЗАМОВНИКА</h3>
            <p class="text-no-padding">3.1. Замовник несе відповідальність за&nbsp;достовірність наданої при оформленні замовлення інформації та&nbsp;її&nbsp;чистоту від претензій третіх осіб. У&nbsp;випадку наявності помилок та/або надання неповних даних в&nbsp;полях &laquo;ПІБ&raquo; та&nbsp;&laquo;Адреса доставки&raquo;, ФОП повністю звільняється від відповідальності за&nbsp;неналежне виконання замовлення.</p>
            <p class="text-no-padding">3.2. Замовник підтверджує свою згоду з&nbsp;умовами, які встановлені цим Договором, при оформлені замовлення на&nbsp;сайті та/або по&nbsp;телефону.</p>
            <p class="text-no-padding">3.3. Використання ресурсу інтернет-сайта для огляду та&nbsp;вибору товару, а&nbsp;також оформлення замовлення є&nbsp;для Замовника безкоштовним.</p>
            <p class="text-no-padding">3.4. Товар замовляється Замовником виключно для особистих, сімейних, побутових потреб, не&nbsp;пов&rsquo;язаних із&nbsp;здійсненням підприємницької діяльності.</p>
            <h3 class="text-no-padding">4. ПРЕДМЕТ ОФЕРТИ</h3>
            <p class="text-no-padding">4.1. ФОП, у&nbsp;якості повіреного відповідно до&nbsp;ст.1000&nbsp;ЦК України, на&nbsp;підставі замовлень Замовника, виконує доручення Замовника (який виступає&nbsp;&mdash; довірителем) на&nbsp;формування замовлення, придбання та&nbsp;доставку товарів від імені та&nbsp;за&nbsp;рахунок Замовника у&nbsp;відповідності із&nbsp;умовами та&nbsp;за&nbsp;цінами, встановленими на&nbsp;сторінках інтернет-сайту.</p>
            <p class="text-no-padding">4.2. Доставка товарів, які були замовлені та&nbsp;придбані Замовником, здійснюється ФОП або третьою особою (Перевізником) за&nbsp;дорученням ФОП. Замовник має право забрати (отримати) товар самостійно. Замовнику при оформлені замовлення надається право вибору способу доставки.</p>
            <p class="text-no-padding">4.3. Фізична або юридична особа вважається такою, яка прийняла всі умови Оферти (акцепт Оферти) в&nbsp;повному обсязі та&nbsp;без виключень з&nbsp;моменту вказаного в&nbsp;п.&nbsp;1.5. цього Договору. У&nbsp;випадку акцепту Оферти одним з&nbsp;вищезазначених способів, фізична або юридична особа вважається такою, що&nbsp;уклала з&nbsp;ФОП даний договір та&nbsp;набуває статусу Замовника.</p>
            <p class="text-no-padding">4.4. Для виконання зобов&rsquo;язань за&nbsp;цим Договором ФОП має право залучати третіх осіб (юридичних осіб та/або фізичних осіб&nbsp;&mdash; підприємців) за&nbsp;договорами доручення, комісії, перевезення тощо.</p>
            <p class="text-no-padding">4.5. ФОП має право передати виконання зобов&rsquo;язань за&nbsp;цим договором іншій особі (замісникові) повністю або в&nbsp;частині на&nbsp;вибір ФОП.</p>
            <p class="text-no-padding">4.6. Сторони домовились, що&nbsp;ФОП виконав свої зобов&rsquo;язання за&nbsp;цим договором після передачі (отримання) Замовнику замовлених Товарів.</p>
            <h3 class="text-no-padding">5. ПОРЯДОК УКЛАДАННЯ ДОГОВОРУ</h3>
            <p class="text-no-padding">5.1. Замовник може оформити замовлення самостійно на&nbsp;сайті або за&nbsp;телефонами, зазначеними на&nbsp;сайті, на&nbsp;умовах даного Договору.</p>
            <p class="text-no-padding">5.2. При оформлені замовлення на&nbsp;сайті Замовник зобов&rsquo;язаний надати про себе наступну інформацію:</p>
            <p class="text-no-padding">&bull; П.І.Б. (для фізичних осіб) або повне найменування, код ЄДРПОУ (для юридичних осіб);</p>
            <p class="text-no-padding">&bull; адресу доставки Товару;</p>
            <p class="text-no-padding">&bull; контактний телефон;</p>
            <p class="text-no-padding">&bull; електронну пошту (за&nbsp;бажанням).</p>
            <p class="text-no-padding">5.3. Волевиявлення Замовника здійснюється шляхом внесення останнім відповідних даних у&nbsp;форму замовлення на&nbsp;сайті або подачі замовлення за&nbsp;телефонами.</p>
            <p class="text-no-padding">5.4. Інтернет-сайт та&nbsp;ФОП можуть здійснюватити редагування інформації замовлення та&nbsp;інформації про Замовника для уточнення лише за&nbsp;згодою Замовника.</p>
            <h3 class="text-no-padding">6. ІНФОРМАЦІЯ ПРО ТОВАР</h3>
            <p class="text-no-padding">6.1. Товар представлений на&nbsp;сайті через фото зразки та/або опис товару, в&nbsp;разі відсутності його зображення.</p>
            <p class="text-no-padding">6.2. Кожний фото зразок супроводжується текстовою інформацією: найменування, розміри (при необхідності), інформаційною ціною (яка може включати вартість доставки та&nbsp;вартість іншіих послуг, які надаються ФОП) та&nbsp;описом товару.</p>
            <h3 class="text-no-padding">7. ПОРЯДОК ЗАМОВЛЕННЯ ТОВАРУ</h3>
            <p class="text-no-padding">7.1. Замовник вправі оформити замовлення на&nbsp;будь-який товар, який представлений на&nbsp;сторінках інтернет-сайту. Кожний товар може бути замовлений в&nbsp;будь-якій кількості. Виключення із&nbsp;зазначеного правила вказані при описі кожного товару у&nbsp;випадку проведення акцій, зняття товару з&nbsp;продажу та&nbsp;інше. Замовлення (доручення на&nbsp;придбання та&nbsp;доставку товара) може бути оформлене Замовником за&nbsp;телефонами, зазначеними на&nbsp;сайті, або оформлене самостійно за&nbsp;допомогою &laquo;електронної корзини&raquo; на&nbsp;сайті.</p>
            <p class="text-no-padding">7.2. Після оформлення замовлення (та/або доручення на&nbsp;придбання та&nbsp;доставку товара) представник ФОПа на&nbsp;контактний телефон Замовника відправляє SMS-повідомдення з&nbsp;підтвердженням прийняття замовлення, а&nbsp;у&nbsp;разі, якщо Замовник вказав E-mail, йому на&nbsp;E-mail може прийти повідомлення, що&nbsp;містить рахунок із&nbsp;зазначенням найменування, розміру, ціни вибраного товару та&nbsp;загальної суми замовлення. ФОП має право змінювати текст повідомлення на&nbsp;власний розсуд. Отримання SMS-повідомдення та/або повідомлення на&nbsp;E-mail Замовником є&nbsp;підтвердженням прийняття замовлення. В&nbsp;подальшому представник ФОПа може зв&rsquo;язатися з&nbsp;Замовником (по&nbsp;телефону або через електрону пошту) для уточнення інформація щодо умов замовлення та&nbsp;доставки.</p>
            <p class="text-no-padding">7.3. При неможливості замовлення, придбання та&nbsp;доставки товару (та/або виконання доручення на&nbsp;придбання та&nbsp;доставку товара) представник ФОПа зобов&rsquo;язаний довести це&nbsp;до&nbsp;відома Замовника (по&nbsp;телефону або через електронну пошту).</p>
            <p class="text-no-padding">7.4. Замовник вправі зробити попереднє замовлення (та/або оформити доручення на&nbsp;придбання та&nbsp;доставку товара) на&nbsp;тимчасово відсутні товари.</p>
            <p class="text-no-padding">7.5. При відсутності товару Замовник вправі замінити його іншим товаром або анулювати замовлення.</p>
            <p class="text-no-padding">7.6. Замовлення обробляється з&nbsp;моменту його отримання.</p>
            <p class="text-no-padding">7.7. Строк виконання замовлення на&nbsp;продаж, придбання та&nbsp;доставку товару зазначається в&nbsp;рахунку та&nbsp;відповідно до&nbsp;заявки Замовника, що&nbsp;подана через веб-сайт в&nbsp;порядку цього Договору.</p>
            <h3 class="text-no-padding">8. ЦІНА ТОВАРУ</h3>
            <p class="text-no-padding">8.1. Ціна товару на&nbsp;сторінках інтернет-сайта зазначається в&nbsp;гривнях за&nbsp;одиницю товару та/або одиницю виміру та&nbsp;є&nbsp;інформаційною.</p>
            <p class="text-no-padding">8.2. Зазначена на&nbsp;сайті ціна товару може бути змінена інтернет-сайтом в&nbsp;односторонньому порядку, при цьому ціна на&nbsp;замовлений Замовником товар не&nbsp;підлягає зміні, якщо він підлягає доставці протягом 6&nbsp;годин з&nbsp;моменту оформлення замовлення. В&nbsp;разі, коли виконання замовлення Замовника (доставка) здійснюється за&nbsp;замовленням Замовника, поданим згідно статті 6&nbsp;цього Договору, після 18&nbsp;години 00&nbsp;хвилин, поточного дня, ціна Товару може бути змінена в&nbsp;односторонньому порядку відповідно до&nbsp;ціни наступного дня (відповідно до&nbsp;щоденної зміни ціни товарів, або зміни ціни у&nbsp;роздрібній мережі та&nbsp;магазині), про що&nbsp;Замовник повідомляється представником інтернет-сайту під час погодження замовлення.</p>
            <p class="text-no-padding">8.3. Повна вартість замовлення складається&nbsp;із:</p>
            <p class="text-no-padding">&mdash;&nbsp;компенсації витрат на&nbsp;придбання від імені та&nbsp;за&nbsp;рахунок Замовника товарів;</p>
            <p class="text-no-padding">&mdash;&nbsp;вартості послуг з&nbsp;доставки та&nbsp;виконання доручення у&nbsp;відповідних замовленнях.</p>
            <p class="text-no-padding">8.4. Детальні інформація про вартість товарів та&nbsp;вартість доставки товарів зазначена на&nbsp;сайті в&nbsp;розділах &laquo;Спосіб доставки&raquo; та&nbsp;&laquo;Адреса доставка&raquo;.</p>
            <p class="text-no-padding">8.5.Відповідно до&nbsp;ст.1002&nbsp;цк України Замовник оплачує ФОП послуги з&nbsp;виконання доручення на&nbsp;прибання та&nbsp;доставку відповідних товарів за&nbsp;умовами визначеними ФОП. Інформаційна ціна на&nbsp;інтернет-сайті може включати суму компенсації за&nbsp;придбання відповідного товару та&nbsp;суму послуг з&nbsp;виконання доручення на&nbsp;придбання та&nbsp;доставку відповідного товара з&nbsp;інтернет-сайта.</p>
            <h3 class="text-no-padding">9. ВІДШКОДУВАННЯ ВИТРАТ</h3>
            <p class="text-no-padding">9.1. Порядок відшкодування витрат ФОП у&nbsp;зв&rsquo;язку з&nbsp;виконанням цього Договору та&nbsp;порядок оплати вартості придбаного товару, зазначений на&nbsp;сайті в&nbsp;розділі &laquo;Спосіб доставки&raquo;. При необхідності порядок та&nbsp;умови відшкодування витрат ФОП з&nbsp;виконання доручення та&nbsp;оптати вартості товарів та&nbsp;послуг обговорюються Замовником з&nbsp;представником інтернет-сайту.</p>
            <p class="text-no-padding">9.2. Відшкодування витрат ФОП у&nbsp;зв&rsquo;язку з&nbsp;виконанням цього Договору та&nbsp;оплата вартості придбаних товарів та&nbsp;послуг здійснюється в&nbsp;готівковій або безготівковій формі. Замовник зобов&rsquo;язаний відшкодувати витрати ФОП у&nbsp;зв&rsquo;язку з&nbsp;виконанням цього Договору та&nbsp;оплатити вартість придбаних товарів до&nbsp;або в&nbsp;момент передачі йому замовленого товару ФОП або перевізником, який здійснює доставку товару. Відшкодування витрат ФОП у&nbsp;зв&rsquo;язку з&nbsp;виконанням цього Договору та&nbsp;оплата вартості придбаних товарів, також, може бути проведена способом безготівкового перерахування грошових коштів.</p>
            <p class="text-no-padding">9.3. У&nbsp;разі оплати замовлення з&nbsp;використанням інтернет-оплати Замовник погоджується, що&nbsp;сума фактичного заказу (доставленого, виконаного) може бути меншою (за&nbsp;рахунок вагових товарів, узгоджених замін, оперативна наявність товару та&nbsp;іншого), ніж сума попередньої оплати, проведеної на&nbsp;підставі попереднього замовлення товарів. Решта попередньої оплати, яка виникла при цьому, не&nbsp;повертається Замовнику, а&nbsp;є&nbsp;сумою авансу відповідного Замовника на&nbsp;наступне Замовлення, та&nbsp;буде зарахована як&nbsp;часткова оплата наступного замовлення. У&nbsp;будь-якому випадку цей аванс (решта попередньої оплату) буде зарахован як&nbsp;часткова оплата наступного замовлення, або буде передан у&nbsp;власність ФОП, якщо не&nbsp;буде використан Замовником (відсутній наступне замовлення) на&nbsp;протязі 370 календарних днів з&nbsp;моменту зарахування на&nbsp;рахунок. Списання авансу в&nbsp;оплату замовлення, або у&nbsp;власність ФОП, відбуваєтьсяв автоматичному режимі за&nbsp;згодою Сторін.</p>
            <p class="text-no-padding">9.4.У разі неможливості виконання замовлення у&nbsp;повному обсязі сума попередньої оплати, отриманої з&nbsp;використанням інтернет-оплати, повертається Замовнику&nbsp;&mdash; платнику на&nbsp;протязі 5&nbsp;робочих днів з&nbsp;моменту отримання від нього заяви у&nbsp;електронному вигляді на&nbsp;адресу&nbsp;&mdash; https://asbam.com.ua/ із&nbsp;зазначенням необхідних платіжних реквізитів для повернення. В&nbsp;іншому випадку така сума оплати зараховується як&nbsp;аванс Замовника на&nbsp;наступне замовлення та&nbsp;використовується у&nbsp;спосіб визначений п.10.3. Договору.</p>
            <p class="text-no-padding">9.5. Розрахунки між Сторонами в&nbsp;рамках цього Договору здійснюються в&nbsp;національній валюті&nbsp;&mdash; гривнях.</p>
            <h3 class="text-no-padding">10. ДОСТАВКА ТОВАРІВ</h3>
            <p class="text-no-padding">10.1. Способи, порядок та&nbsp;строки доставки товару зазначені на&nbsp;сайті в&nbsp;розділах &laquo;Спосіб доставки&raquo; та&nbsp;&laquo;Адреса доставка&raquo;. Порядок та&nbsp;умови доставки замовленого товару погоджуються Замовником з&nbsp;представником ФОПа.</p>
            <p class="text-no-padding">10.2. Самовивіз товару:</p>
            <p class="text-no-padding">10.2.1. Замовник отримує товар за&nbsp;Замовленням за&nbsp;місцем узгодженим з&nbsp;ФОП. Адреса та&nbsp;режим роботи зазначені на&nbsp;сайті https://asbam.com.ua/ в&nbsp;розділі &laquo;Адреса доставки&raquo;.</p>
            <p class="text-no-padding">10.2.2. Право власності та&nbsp;ризик випадкової загибелі, втрати чи&nbsp;пошкодження товару переходить до&nbsp;Замовника з&nbsp;моменту передачі товару Замовнику або його Представнику шляхом підписання Сторонами товарного чеку та/або замовлення (та/або доручення на&nbsp;придбання та&nbsp;доставку товара) на&nbsp;доставку.</p>
            <p class="text-no-padding">10.3. Доставка товару здійснюється власними силами ФОП відповідно до&nbsp;умов доставки замовленого товару, або із&nbsp;залученням третіх осіб (перевізника).</p>
            <p class="text-no-padding">10.3.1. Право власності та&nbsp;ризик випадкової загибелі, втрати чи&nbsp;пошкодження товару переходить до&nbsp;Замовника з&nbsp;моменту передачі товару Замовнику або його Представнику шляхом підписання Сторонами товарного чеку та/або замовлення на&nbsp;доставку.</p>
            <p class="text-no-padding">10.3.2. При доставці товар передається Замовнику або Представнику Замовника.</p>
            <p class="text-no-padding">10.4. Вартість доставки товару в&nbsp;рамках кожного замовлення розраховується виходячи із&nbsp;ваги всіх замовлених товарів, адреси доставки замовлення, тарифів на&nbsp;доставку, які описані на&nbsp;сайті в&nbsp;розділі &laquo;Спосіб доставки&raquo; та&nbsp;оплачується Замовником.</p>
            <p class="text-no-padding">10.5. Замовник зобов&rsquo;язаний прийняти товар в&nbsp;кількості та&nbsp;асортименті в&nbsp;момент його приймання.</p>
            <p class="text-no-padding">10.6. При отриманні товару Замовник повинен в&nbsp;присутності представника ФОП перевірити відповідність Товару якісним та&nbsp;кількісним характеристикам, що&nbsp;зазначені в&nbsp;товарному чеку та/або замовленні (дореченні) на&nbsp;доставку (найменування товару кількість, комплектність, тощо).</p>
            <p class="text-no-padding">10.7. Замовник або Представник Замовника при прийманні товару підтверджує своїм підписом в&nbsp;товарному чеку та/або замовленні на&nbsp;доставку товарів, що&nbsp;не&nbsp;має претензій до&nbsp;кількості товару, зовнішнього виду та&nbsp;комплектності товару.</p>
            <h3 class="text-no-padding">11. ГАРАНТІЇ НА&nbsp;ТОВАР</h3>
            <p class="text-no-padding">11.1. Строк придатності Товару (-ів) встановлюється Виробником та&nbsp;позначається на&nbsp;упаковці Товару (-ів).</p>
            <h3 class="text-no-padding">12. ВІДПОВІДАЛЬНІСТЬ СТОРІН</h3>
            <p class="text-no-padding">12.1. Сторони несуть відповідальність передбачену діючим законодавства України та&nbsp;цим Договором.</p>
            <p class="text-no-padding">12.2. ФОП не&nbsp;несе відповідальності за&nbsp;шкоду, яка була нанесена Замовнику внаслідок неналежного використання ним товарів, замовлених на&nbsp;інтернет-сайті.</p>
            <p class="text-no-padding">12.3. Сторони звільняються від відповідальності за&nbsp;невиконання або неналежне виконання зобов&rsquo;язань за&nbsp;цим Договором на&nbsp;час дії обставин непереборної сили.</p>
            <h3 class="text-no-padding">13. ІНШІ УМОВИ</h3>
            <p class="text-no-padding">13.1. До&nbsp;правовідносин між Замовником та&nbsp;ФОП застосовується діюче законодавство України.</p>
            <p class="text-no-padding">13.2. У&nbsp;випадку виникнення питань та&nbsp;претензій з&nbsp;боку Замовника він повинен звернутися до&nbsp;Центру обслуговування клієнтів за&nbsp;телефоном: +38&nbsp;067&nbsp;011 22 02.</p>
            <p class="text-no-padding">13.3. Цей Договір вступає в&nbsp;силу з&nbsp;моменту акцепту Замовником цієї Оферти, відповідно до&nbsp;п.1.5&nbsp;Договору, та&nbsp;діє до&nbsp;повного виконання своїх зобов&rsquo;язань Сторонами.</p>
            <p class="text-no-padding">13.4. Всі спори та&nbsp;суперечки, які виникають при виконані Сторонами зобов&rsquo;язань по&nbsp;цьому Договору, вирішуються шляхом переговорів. У&nbsp;випадку неможливості їх&nbsp;усунення, Сторони мають право звернутися за&nbsp;захистом своїх прав та&nbsp;інтересів в&nbsp;судовому порядку.</p>
            <h3 class="text-no-padding">14. ЗАХИСТ ПЕРСОНАЛЬНИХ ДАНИХ</h3>
            <p class="text-no-padding">14.1. При реєстрації на&nbsp;інтернет-сайті Замовник залишає свої персональні дані, в&nbsp;тому числі:</p>
            <p class="text-no-padding">&mdash;&nbsp;прізвище, ім&rsquo;я, по-батькові;</p>
            <p class="text-no-padding">&mdash;&nbsp;адреса доставки;</p>
            <p class="text-no-padding">&mdash;&nbsp;номер телефону;</p>
            <p class="text-no-padding">&mdash;&nbsp;електронну адреса (e-mail);</p>
            <p class="text-no-padding">14.2. Надаючи свої персональні дані при реєстрації на&nbsp;інтернет-сайті, Замовник дає свою добровільну безвідкличну згоду на&nbsp;обробку і&nbsp;використання (у&nbsp;тому числі і&nbsp;передачу) своїх персональних даних без обмеження терміну дії такої згоди відповідно до&nbsp;Закону України &laquo;Про захист персональних даних&raquo; від 01.06.2010р.</p>
            <p class="text-no-padding">14.3. ФОП використовує отримані Персональні дані для цілей виконання доручення і&nbsp;надання послуг, визначених цим Договором, для просування послуг, що&nbsp;надаються ФОП, у&nbsp;тому числі і&nbsp;за&nbsp;допомогою автоматизованої обробки персональних даних.</p>
            <p class="text-no-padding">14.4. ФОП та&nbsp;інтернет-сайт зобов&rsquo;язуються не&nbsp;розголошувати отриману від Замовника інформацію. Не&nbsp;вважається порушенням надання ФОП та&nbsp;інтернет-сайтом інформації агентам і&nbsp;третім особам, що&nbsp;діють на&nbsp;підставі договору з&nbsp;ФОП, у&nbsp;тому числі і&nbsp;для виконання зобов&rsquo;язань перед Замовником, а&nbsp;також у&nbsp;випадках, коли розкриття такої інформації встановлене вимогами законодавства.</p>
            <p class="text-no-padding">14.5. Замовник несе відповідальність за&nbsp;підтримку своїх персональних даних в&nbsp;актуальному стані. ФОП та&nbsp;інтернет-сайт не&nbsp;несуть відповідальності за&nbsp;неякісне виконання або невиконання своїх зобов&rsquo;язань у&nbsp;зв&rsquo;язку з&nbsp;неактуальністю інформації про Замовника або невідповідністю її&nbsp;дійсності.</p>
            <h3 class="text-no-padding">АДРЕСА ТА&nbsp;РЕКВІЗИТИ</h3>
            <p class="text-no-padding"><strong>ФОП Мазур Андрій Васильович</strong></p>
            <p class="text-no-padding text-small">Адреса: 82094, Львівська обл., Старосамбірський район, село Головецько</p>
            <p class="text-no-padding text-small">Ідентифікаційний код: 3309415333</p>
            <p class="text-no-padding text-small">р/р 26009017977901 Банк отримувач: ПАТ &laquo;АЛЬФА-БАНК&raquo;</p>
            <p class="text-no-padding text-small">МФО 300346</p>
            <p class="text-no-padding text-small">Є&nbsp;платником єдиного податку</p>
            <p class="text-no-padding text-small">Не&nbsp;є&nbsp;платником ПДВ</p>
		</div>
	</div>
</div>
<footer class="site-footer">
	<div class="inner-wrapper clearfix">
		<div class="copyright">
            Copyright 2020 | <span class="red">Аптека "БАМ"</span>
            <a href="https://www.facebook.com/bam.ukr/" target="_blank" rel="nofollow"><i class="icon icon-fb"></i></a>
        </div>
		<div class="author"><span>Розміщення інформації здійснює ФОП Мазур А.В. <a href="#" class="btn-contract">Публічний договір</a></span></div>
	</div>
</footer>
	<script type="text/javascript">
<!--
	var cookieDomain = '.asbam.com.ua',
	    cookiePath = '/',
        Warehouses = new WarehousesRepository([{"ext_id":128,"city_id":2054,"is_default":false,"link":"https:\/\/goo.gl\/maps\/Lniok5MbCjv","address":"\u0432\u0443\u043b. \u0428\u0438\u0440\u043e\u043a\u0430, 64 (\u041b\u0435\u0432\u0430\u043d\u0434\u0456\u0432\u043a\u0430)","timetable":"<p>\u0429\u043e\u0434\u0435\u043d\u043d\u043e \u0437  <strong>8<sup>00<\/sup><\/strong> \u0434\u043e <strong>21<sup>00<\/sup><\/strong><\/p>"},{"ext_id":134,"city_id":2052,"is_default":false,"link":"https:\/\/goo.gl\/maps\/XLwaW54V2Rn","address":"\u043f\u0440\u043e\u0441\u043f. \u0412\u0456\u0434\u0440\u043e\u0434\u0436\u0435\u043d\u043d\u044f, \u0431\u0443\u0434. 26\u0430","timetable":"<p>\u041f\u043e\u043d\u0435\u0434\u0456\u043b\u043e\u043a \u2013 \u041f\u2019\u044f\u0442\u043d\u0438\u0446\u044f \u0437 <strong>8<sup>00<\/sup><\/strong> \u0434\u043e <strong>22<sup>00<\/sup><\/strong><\/p>\r\n<p>\u0421\u0443\u0431\u043e\u0442\u0430 \u0437 <strong>8<sup>00<\/sup><\/strong> \u0434\u043e <strong>20<sup>00<\/sup><\/strong><\/p>\r\n<p>\u041d\u0435\u0434\u0456\u043b\u044f \u0437 <strong>9<sup>00<\/sup><\/strong> \u0434\u043e <strong>19<sup>00<\/sup><\/strong><\/p>"},{"ext_id":156,"city_id":1946,"is_default":false,"link":"https:\/\/goo.gl\/2o504v","address":"\u0432\u0443\u043b. \u0413\u0430\u043b\u0438\u0446\u044c\u043a\u0430, \u0431\u0443\u0434. 80\u0431","timetable":"<p>\u041f\u043e\u043d\u0435\u0434\u0456\u043b\u043e\u043a \u2013 \u041f\u2019\u044f\u0442\u043d\u0438\u0446\u044f \u0437 <strong>8<sup>00<\/sup><\/strong> \u0434\u043e <strong>21<sup>00<\/sup><\/strong><\/p>\r\n<p>\u0421\u0443\u0431\u043e\u0442\u0430 \u0437 <strong>9<sup>00<\/sup><\/strong> \u0434\u043e <strong>20<sup>00<\/sup><\/strong><\/p>\r\n<p>\u041d\u0435\u0434\u0456\u043b\u044f \u0437 <strong>9<sup>00<\/sup><\/strong> \u0434\u043e <strong>20<sup>00<\/sup><\/strong><\/p>"},{"ext_id":158,"city_id":2054,"is_default":false,"link":"https:\/\/goo.gl\/kq4Jle","address":"\u0432\u0443\u043b. \u0421\u0442\u0440\u0438\u0439\u0441\u044c\u043a\u0430, \u0431\u0443\u0434. 51","timetable":"<p>\u041f\u043e\u043d\u0435\u0434\u0456\u043b\u043e\u043a \u2013 \u041d\u0435\u0434\u0456\u043b\u044f \u0437 <strong>8<sup>00<\/sup><\/strong> \u0434\u043e <strong>21<sup>00<\/sup><\/strong><\/p>\r\n"},{"ext_id":170,"city_id":2054,"is_default":false,"link":"https:\/\/goo.gl\/mEU5TF","address":"\u0432\u0443\u043b. \u0413\u043e\u0440\u043e\u0434\u043e\u0446\u044c\u043a\u0430, \u0431\u0443\u0434. 82","timetable":"<p>\u041f\u043e\u043d\u0435\u0434\u0456\u043b\u043e\u043a \u2013 \u041f\u2019\u044f\u0442\u043d\u0438\u0446\u044f \u0437 <strong>7<sup>45<\/sup><\/strong> \u0434\u043e <strong>21<sup>15<\/sup><\/strong><\/p>\r\n<p>\u0421\u0443\u0431\u043e\u0442\u0430 \u0437 <strong>7<sup>45<\/sup><\/strong> \u0434\u043e <strong>20<sup>15<\/sup><\/strong><\/p>\r\n<p>\u041d\u0435\u0434\u0456\u043b\u044f \u0437 <strong>8<sup>45<\/sup><\/strong> \u0434\u043e <strong>20<sup>15<\/sup><\/strong><\/p>\r\n"},{"ext_id":185,"city_id":1844,"is_default":false,"link":"https:\/\/goo.gl\/maps\/8twtzS6v5g62","address":"\u0432\u0443\u043b.\u0425\u043c\u0435\u043b\u044c\u043d\u0438\u0446\u044c\u043a\u0435 \u0448\u043e\u0441\u0435, 108\u0430","timetable":"<p>\u041f\u043e\u043d\u0435\u0434\u0456\u043b\u043e\u043a \u2013 \u041f\u2019\u044f\u0442\u043d\u0438\u0446\u044f \u0437 <strong>8<sup>00<\/sup><\/strong> \u0434\u043e <strong>21<sup>00<\/sup><\/strong><\/p>\r\n<p>\u0421\u0443\u0431\u043e\u0442\u0430 \u0437 <strong>8<sup>00<\/sup><\/strong> \u0434\u043e <strong>20<sup>00<\/sup><\/strong><\/p>\r\n<p>\u041d\u0435\u0434\u0456\u043b\u044f \u0437 <strong>8<sup>00<\/sup><\/strong> \u0434\u043e <strong>20<sup>00<\/sup><\/strong><\/p>\r\n"},{"ext_id":94,"city_id":2054,"is_default":false,"link":"https:\/\/goo.gl\/maps\/MZbHP2H2hQK2","address":"\u0432\u0443\u043b.\u041a\u043b\u0435\u043f\u0430\u0440\u0456\u0432\u0441\u044c\u043a\u0430,4","timetable":"<p>\u041f\u043e\u043d\u0435\u0434\u0456\u043b\u043e\u043a \u2013 \u041f\u2019\u044f\u0442\u043d\u0438\u0446\u044f \u0437 <strong>8<sup>00<\/sup><\/strong> \u0434\u043e <strong>20<sup>00<\/sup><\/strong><\/p>\n<p>\u0421\u0443\u0431\u043e\u0442\u0430 \u0437 <strong>9<sup>00<\/sup><\/strong> \u0434\u043e <strong>18<sup>00<\/sup><\/strong><\/p>\n<p>\u041d\u0435\u0434\u0456\u043b\u044f \u0437 <strong>9<sup>00<\/sup><\/strong> \u0434\u043e <strong>18<sup>00<\/sup><\/strong><\/p>\n"},{"ext_id":754,"city_id":1642,"is_default":false,"link":"","address":"\u0432\u0443\u043b. \u0421\u043e\u0431\u043e\u0440\u043d\u0430 260","timetable":"<p>\u041f\u043e\u043d\u0435\u0434\u0456\u043b\u043e\u043a \u2013 \u0421\u0443\u0431\u043e\u0442\u0430 \u0437 <strong>8<sup>00<\/sup><\/strong> \u0434\u043e <strong>21<sup>00<\/sup><\/strong><\/p>\r\n<p>\u041d\u0435\u0434\u0456\u043b\u044f <strong>8<sup>00<\/sup><\/strong> \u0434\u043e <strong>20<sup>00<\/sup><\/strong><\/p>\r\n"},{"ext_id":217,"city_id":1976,"is_default":false,"link":"","address":"\u0432\u0443\u043b.\u0420\u0435\u0432\u0443\u0446\u044c\u043a\u043e\u0433\u043e, 12\u0430","timetable":"<p>\u041f\u043d-\u041d\u0434 \u0437  <strong>8<sup>00<\/sup><\/strong> \u0434\u043e <strong>21<sup>00<\/sup><\/strong><\/p>\r\n"},{"ext_id":220,"city_id":1920,"is_default":false,"link":"","address":"\u0432\u0443\u043b. \u041a\u0438\u0457\u0432\u0441\u044c\u043a\u0430 25","timetable":"<p>\u041f\u043e\u043d\u0435\u0434\u0456\u043b\u043e\u043a \u2013 \u041f\u2019\u044f\u0442\u043d\u0438\u0446\u044f \u0437 <strong>8<sup>00<\/sup><\/strong> \u0434\u043e <strong>21<sup>00<\/sup><\/strong><\/p>\n<p>\u0421\u0443\u0431\u043e\u0442\u0430,\u041d\u0435\u0434\u0456\u043b\u044f <strong>9<sup>00<\/sup><\/strong> \u0434\u043e <strong>20<sup>00<\/sup><\/strong><\/p>"},{"ext_id":231,"city_id":1976,"is_default":false,"link":"","address":"\u043f\u0440\u043e\u0441\u043f\u0435\u043a\u0442 \u041c\u0430\u044f\u043a\u043e\u0432\u0441\u044c\u043a\u043e\u0433\u043e \u0412\u043e\u043b\u043e\u0434\u0438\u043c\u0438\u0440\u0430 60\/10","timetable":"<p>\u041f\u043d-\u041d\u0434 \u0437  <strong>8<sup>00<\/sup><\/strong> \u0434\u043e <strong>21<sup>00<\/sup><\/strong><\/p>\r\n"},{"ext_id":162,"city_id":2023,"is_default":false,"link":"","address":"\u0432\u0443\u043b. \u0428\u0435\u0432\u0447\u0435\u043d\u043a\u0430 46\u0430","timetable":"<p>\u041f\u043e\u043d\u0435\u0434\u0456\u043b\u043e\u043a \u2013 \u041f\u2019\u044f\u0442\u043d\u0438\u0446\u044f \u0437 <strong>8<sup>00<\/sup><\/strong> \u0434\u043e <strong>21<sup>00<\/sup><\/strong><\/p>\r\n<p>\u0421\u0443\u0431\u043e\u0442\u0430 \u0437 <strong>8<sup>00<\/sup><\/strong> \u0434\u043e <strong>20<sup>00<\/sup><\/strong><\/p>\r\n<p>\u041d\u0435\u0434\u0456\u043b\u044f \u0437 <strong>9<sup>00<\/sup><\/strong> \u0434\u043e <strong>19<sup>00<\/sup><\/strong><\/p>"},{"ext_id":248,"city_id":2030,"is_default":false,"link":"https:\/\/goo.gl\/maps\/5Wqh43hc7i2182RB6","address":"\u0432\u0443\u043b.\u0410.\u0414\u043e\u043b\u0435\u0439\u043a\u0430,14\u0430","timetable":"<p>\u041f\u043e\u043d\u0435\u0434\u0456\u043b\u043e\u043a \u2013 \u041d\u0435\u0434\u0456\u043b\u044f \u0437 <strong>8<sup>00<\/sup><\/strong> \u0434\u043e <strong>20<sup>00<\/sup><\/strong><\/p>"},{"ext_id":150,"city_id":2111,"is_default":false,"link":"","address":"15-\u0438\u0439 \u041c\u0456\u043a\u0440\u043e\u0440\u0430\u0439\u043e\u043d,19","timetable":"<p>\u041f\u043d-\u0421\u0431 \u0437  <strong>8<sup>00<\/sup><\/strong> \u0434\u043e <strong>21<sup>00<\/sup><\/strong><\/p>\r\n<p>\u041d\u0434 \u0437  <strong>9<sup>00<\/sup><\/strong> \u0434\u043e <strong>20<sup>00<\/sup><\/strong><\/p>"},{"ext_id":265,"city_id":2896,"is_default":false,"link":"","address":"\u0431\u0443\u043b\u044c\u0432\u0430\u0440 \u041e.\u0414\u043e\u0432\u0436\u0435\u043d\u043a\u0430, 12","timetable":"<p>\u041f\u043d-\u0421\u0431 \u0437  <strong>8<sup>00<\/sup><\/strong> \u0434\u043e <strong>21<sup>00<\/sup><\/strong><\/p>\r\n<p>\u041d\u0434 \u0437  <strong>9<sup>00<\/sup><\/strong> \u0434\u043e <strong>18<sup>00<\/sup><\/strong><\/p>"},{"ext_id":259,"city_id":1642,"is_default":false,"link":"","address":"\u0432\u0443\u043b. \u041a\u043d\u044f\u0437\u044f \u0420\u043e\u043c\u0430\u043d\u0430, 9","timetable":"<p>\u041f\u043e\u043d\u0435\u0434\u0456\u043b\u043e\u043a \u2013 \u041f\u2019\u044f\u0442\u043d\u0438\u0446\u044f \u0437 <strong>8<sup>00<\/sup><\/strong> \u0434\u043e <strong>22<sup>00<\/sup><\/strong><\/p>\r\n<p>\u0421\u0443\u0431\u043e\u0442\u0430,\u041d\u0435\u0434\u0456\u043b\u044f <strong>8<sup>00<\/sup><\/strong> \u0434\u043e <strong>21<sup>00<\/sup><\/strong><\/p>"},{"ext_id":253,"city_id":1844,"is_default":false,"link":"","address":"\u0432\u0443\u043b. \u0413\u0440\u0438\u0431\u043e\u0454\u0434\u043e\u0432\u0430 3","timetable":"<p>\u041f\u043e\u043d\u0435\u0434\u0456\u043b\u043e\u043a \u2013 \u041d\u0435\u0434\u0456\u043b\u044f \u0437 <strong>8<sup>00<\/sup><\/strong> \u0434\u043e <strong>21<sup>00<\/sup><\/strong><\/p>"},{"ext_id":261,"city_id":1698,"is_default":false,"link":"","address":"\u043f\u0440\u043e\u0441\u043f\u0435\u043a\u0442 \u0411\u0430\u043d\u0434\u0435\u0440\u0438, 96      ","timetable":"<p>\u041f\u043e\u043d\u0435\u0434\u0456\u043b\u043e\u043a \u2013 \u041f\u2019\u044f\u0442\u043d\u0438\u0446\u044f \u0437 <strong>8<sup>00<\/sup><\/strong> \u0434\u043e <strong>21<sup>00<\/sup><\/strong><\/p>\r\n<p>\u0421\u0443\u0431\u043e\u0442\u0430,\u041d\u0435\u0434\u0456\u043b\u044f <strong>9<sup>00<\/sup><\/strong> \u0434\u043e <strong>20<sup>00<\/sup><\/strong><\/p>"},{"ext_id":266,"city_id":1946,"is_default":false,"link":"","address":"\u0432\u0443\u043b.\u0424\u0435\u0434\u044c\u043a\u043e\u0432\u0438\u0447\u0430, 7\u0431              ","timetable":"<p>\u041f\u043e\u043d\u0435\u0434\u0456\u043b\u043e\u043a \u2013 \u0421\u0443\u0431\u043e\u0442\u0430 \u0437 <strong>8<sup>00<\/sup><\/strong> \u0434\u043e <strong>21<sup>00<\/sup><\/strong><\/p>\r\n<p>\u041d\u0435\u0434\u0456\u043b\u044f <strong>9<sup>00<\/sup><\/strong> \u0434\u043e <strong>20<sup>00<\/sup><\/strong><\/p>"},{"ext_id":177,"city_id":1920,"is_default":false,"link":"","address":"\u0432\u0443\u043b.\u0412.\u0411\u0435\u0440\u0434\u0438\u0447\u0456\u0432\u0441\u044c\u043a\u0430,95","timetable":"<p>\u041f\u043e\u043d\u0435\u0434\u0456\u043b\u043e\u043a \u2013 \u0421\u0443\u0431\u043e\u0442\u0430 \u0437 <strong>8<sup>00<\/sup><\/strong> \u0434\u043e <strong>21<sup>00<\/sup><\/strong><\/p>\r\n<p>\u041d\u0435\u0434\u0456\u043b\u044f <strong>9<sup>00<\/sup><\/strong> \u0434\u043e <strong>20<sup>00<\/sup><\/strong><\/p>"},{"ext_id":288,"city_id":1718,"is_default":false,"link":"","address":"\u0432\u0443\u043b. \u0421\u0432\u043e\u0431\u043e\u0434\u0438, \u0431\u0443\u0434. 1\/\u0430","timetable":"<p>\u041f\u043e\u043d\u0435\u0434\u0456\u043b\u043e\u043a \u2013 \u041d\u0435\u0434\u0456\u043b\u044f \u0437 <strong>8<sup>00<\/sup><\/strong> \u0434\u043e <strong>21<sup>00<\/sup><\/strong><\/p>"},{"ext_id":319,"city_id":1779,"is_default":false,"link":"","address":"\u0432\u0443\u043b. \u041b\u0435\u0432\u0430\u043d\u0435\u0432\u0441\u044c\u043a\u043e\u0433\u043e 57, \u043f\u0440\u0438\u043c. 266 ","timetable":"<p>\u041f\u043e\u043d\u0435\u0434\u0456\u043b\u043e\u043a \u2013 \u041d\u0435\u0434\u0456\u043b\u044f \u0437 <strong>8<sup>00<\/sup><\/strong> \u0434\u043e <strong>21<sup>00<\/sup><\/strong><\/p>\r\n"},{"ext_id":344,"city_id":1687,"is_default":false,"link":"","address":"\u0432\u0443\u043b. \u041b\u0435\u0432\u0430\u043d\u0435\u0432\u0441\u044c\u043a\u043e\u0433\u043e 10\/1","timetable":"<p>\u041f\u043e\u043d\u0435\u0434\u0456\u043b\u043e\u043a \u2013 \u041f\u2019\u044f\u0442\u043d\u0438\u0446\u044f \u0437 <strong>8<sup>00<\/sup><\/strong> \u0434\u043e <strong>21<sup>00<\/sup><\/strong><\/p>\r\n<p>\u0421\u0443\u0431\u043e\u0442\u0430, \u041d\u0435\u0434\u0456\u043b\u044f \u0437 <strong>9<sup>00<\/sup><\/strong> \u0434\u043e <strong>20<sup>00<\/sup><\/strong><\/p>\r\n"},{"ext_id":346,"city_id":1642,"is_default":false,"link":"","address":"\u0432\u0443\u043b. \u0421.\u0411\u0430\u043d\u0434\u0435\u0440\u0438, 49","timetable":"<p>\u041f\u043e\u043d\u0435\u0434\u0456\u043b\u043e\u043a \u2013 \u0421\u0443\u0431\u043e\u0442\u0430 \u0437 <strong>8<sup>00<\/sup><\/strong> \u0434\u043e <strong>21<sup>00<\/sup><\/strong><\/p>\r\n<p>\u041d\u0435\u0434\u0456\u043b\u044f <strong>9<sup>00<\/sup><\/strong> \u0434\u043e <strong>20<sup>00<\/sup><\/strong><\/p>"},{"ext_id":379,"city_id":1978,"is_default":false,"link":"","address":"\u0432\u0443\u043b.\u041f\u0430\u0448\u0443\u0442\u0438\u043d\u0441\u044c\u043a\u0430, 75","timetable":"<p>\u041f\u043e\u043d\u0435\u0434\u0456\u043b\u043e\u043a \u2013 \u041f'\u044f\u0442\u043d\u0438\u0446\u044f \u0437 <strong>8<sup>00<\/sup><\/strong> \u0434\u043e <strong>21<sup>00<\/sup><\/strong><\/p>\r\n<p>\u0421\u0443\u0431\u043e\u0442\u0430 - \u041d\u0435\u0434\u0456\u043b\u044f <strong>9<sup>00<\/sup><\/strong> \u0434\u043e <strong>20<sup>00<\/sup><\/strong><\/p>"},{"ext_id":386,"city_id":1728,"is_default":false,"link":"","address":"\u043f\u0440.\u041f\u0435\u0440\u0435\u043c\u043e\u0433\u0438, 14","timetable":"<p>\u041f\u043e\u043d\u0435\u0434\u0456\u043b\u043e\u043a \u2013 \u041f'\u044f\u0442\u043d\u0438\u0446\u044f \u0437 <strong>8<sup>00<\/sup><\/strong> \u0434\u043e <strong>21<sup>00<\/sup><\/strong><\/p>\r\n<p>\u0421\u0443\u0431\u043e\u0442\u0430 - \u041d\u0435\u0434\u0456\u043b\u044f <strong>9<sup>00<\/sup><\/strong> \u0434\u043e <strong>20<sup>00<\/sup><\/strong><\/p>"},{"ext_id":398,"city_id":2054,"is_default":false,"link":"","address":"\u0432\u0443\u043b. \u0421\u0438\u0445\u0456\u0432\u0441\u044c\u043a\u0430, 8","timetable":"<p>\u041f\u043e\u043d\u0435\u0434\u0456\u043b\u043e\u043a \u2013 \u041d\u0435\u0434\u0456\u043b\u044f \u0437 <strong>8<sup>00<\/sup><\/strong> \u0434\u043e <strong>20<sup>00<\/sup><\/strong><\/p>\r\n"},{"ext_id":383,"city_id":2027,"is_default":false,"link":"","address":"\u043f\u043b. \u041e.\u041f\u043e\u043b\u044f 1, \u043f\u0440\u0438\u043c. 120","timetable":"<p>\u041f\u043e\u043d\u0435\u0434\u0456\u043b\u043e\u043a \u2013 \u041d\u0435\u0434\u0456\u043b\u044f \u0437 <strong>8<sup>00<\/sup><\/strong> \u0434\u043e <strong>21<sup>00<\/sup><\/strong><\/p>"},{"ext_id":392,"city_id":1625,"is_default":false,"link":"","address":"\u0432\u0443\u043b. \u0410\u043b\u043c\u0430\u0437\u043d\u0430 6\/11","timetable":"<p>\u041f\u043e\u043d\u0435\u0434\u0456\u043b\u043e\u043a \u2013 \u041f\u2019\u044f\u0442\u043d\u0438\u0446\u044f \u0437 <strong>7<sup>45<\/sup><\/strong> \u0434\u043e <strong>21<sup>15<\/sup><\/strong><\/p>\r\n<p>\u0421\u0443\u0431\u043e\u0442\u0430 \u0437 <strong>7<sup>45<\/sup><\/strong> \u0434\u043e <strong>20<sup>15<\/sup><\/strong><\/p>\r\n<p>\u041d\u0435\u0434\u0456\u043b\u044f \u0437 <strong>8<sup>45<\/sup><\/strong> \u0434\u043e <strong>20<sup>15<\/sup><\/strong><\/p>\r\n"},{"ext_id":394,"city_id":1727,"is_default":false,"link":"","address":"\u0431-\u0440 \u0428\u0435\u0432\u0447\u0435\u043d\u043a\u0430, 320","timetable":"<p>\u041f\u043e\u043d\u0435\u0434\u0456\u043b\u043e\u043a \u2013 \u041f\u2019\u044f\u0442\u043d\u0438\u0446\u044f \u0437 <strong>7<sup>45<\/sup><\/strong> \u0434\u043e <strong>21<sup>15<\/sup><\/strong><\/p>\r\n<p>\u0421\u0443\u0431\u043e\u0442\u0430 \u0437 <strong>7<sup>45<\/sup><\/strong> \u0434\u043e <strong>20<sup>15<\/sup><\/strong><\/p>\r\n<p>\u041d\u0435\u0434\u0456\u043b\u044f \u0437 <strong>8<sup>45<\/sup><\/strong> \u0434\u043e <strong>20<sup>15<\/sup><\/strong><\/p>\r\n"},{"ext_id":472,"city_id":2054,"is_default":false,"link":"","address":"\u0432\u0443\u043b. \u041c\u0430\u0437\u0435\u043f\u0438, 10","timetable":"<p>\u041f\u043e\u043d\u0435\u0434\u0456\u043b\u043e\u043a \u2013 \u041f\u2019\u044f\u0442\u043d\u0438\u0446\u044f \u0437 <strong>8<sup>00<\/sup><\/strong> \u0434\u043e <strong>20<sup>00<\/sup><\/strong><\/p>\r\n<p>\u0421\u0443\u0431\u043e\u0442\u0430 - \u041d\u0435\u0434\u0456\u043b\u044f \u0437 <strong>8<sup>00<\/sup><\/strong> \u0434\u043e <strong>20<sup>00<\/sup><\/strong><\/p>\r\n"},{"ext_id":574,"city_id":1687,"is_default":false,"link":"","address":"\u043f\u0440\u043e\u0441\u043f\u0435\u043a\u0442 \u041a\u0443\u0440\u0441\u044c\u043a\u0438\u0439, 115","timetable":"<p>\u041f\u043e\u043d\u0435\u0434\u0456\u043b\u043e\u043a \u2013 \u041f\u2019\u044f\u0442\u043d\u0438\u0446\u044f \u0437 <strong>8<sup>00<\/sup><\/strong> \u0434\u043e <strong>21<sup>00<\/sup><\/strong><\/p>\r\n<p>\u0421\u0443\u0431\u043e\u0442\u0430, \u041d\u0435\u0434\u0456\u043b\u044f \u0437 <strong>9<sup>00<\/sup><\/strong> \u0434\u043e <strong>20<sup>00<\/sup><\/strong><\/p>\r\n"},{"ext_id":586,"city_id":1729,"is_default":false,"link":"","address":"\u043f\u0440\u043e\u0441\u043f\u0435\u043a\u0442 \u041d\u0435\u0437\u0430\u043b\u0435\u0436\u043d\u043e\u0441\u0442\u0456, 91","timetable":"<p>\u041f\u043e\u043d\u0435\u0434\u0456\u043b\u043e\u043a \u2013 \u0421\u0443\u0431\u043e\u0442\u0430 \u0437 <strong>8<sup>00<\/sup><\/strong> \u0434\u043e <strong>21<sup>00<\/sup><\/strong><\/p>\r\n<p>\u041d\u0435\u0434\u0456\u043b\u044f \u0437 <strong>9<sup>00<\/sup><\/strong> \u0434\u043e <strong>20<sup>00<\/sup><\/strong><\/p>\r\n"},{"ext_id":672,"city_id":1638,"is_default":false,"link":"","address":"\u0432\u0443\u043b. \u0412\u043e\u0437\u043d\u0435\u0441\u0435\u043d\u0441\u044c\u043a\u0430, 165\/4","timetable":"<p>\u041f\u043e\u043d\u0435\u0434\u0456\u043b\u043e\u043a \u2013 \u041d\u0435\u0434\u0456\u043b\u044f \u0437 <strong>8<sup>00<\/sup><\/strong> \u0434\u043e <strong>20<sup>00<\/sup><\/strong><\/p>\r\n\r\n"},{"ext_id":629,"city_id":1698,"is_default":false,"link":"","address":"\u0432\u0443\u043b.\u041f\u0438\u0440\u043e\u0433\u043e\u0432\u0430, 8\/1  ","timetable":"<p>\u041f\u043e\u043d\u0435\u0434\u0456\u043b\u043e\u043a \u2013 \u0421\u0443\u0431\u043e\u0442\u0430 \u0437 <strong>8<sup>00<\/sup><\/strong> \u0434\u043e <strong>21<sup>00<\/sup><\/strong><\/p>\r\n<p>\u041d\u0435\u0434\u0456\u043b\u044f <strong>8<sup>00<\/sup><\/strong> \u0434\u043e <strong>20<sup>00<\/sup><\/strong><\/p>\r\n"},{"ext_id":653,"city_id":1698,"is_default":false,"link":"","address":"\u0432\u0443\u043b.\u0428\u0435\u043f\u0442\u0438\u0446\u044c\u043e\u0433\u043e \u041c\u0438\u0442\u0440\u043e\u043f\u043e\u043b\u0438\u0442\u0430 1\u043f\u0440\u0438\u043c.76                           ","timetable":"<p>\u041f\u041d-\u0421\u0411 \u0437 <strong>8<sup>00<\/sup><\/strong> \u0434\u043e <strong>20<sup>00<\/sup><\/strong><\/p>\r\n<p>\u041d\u0414 \u0437 <strong>9<sup>00<\/sup><\/strong> \u0434\u043e <strong>19<sup>00<\/sup><\/strong><\/p>"},{"ext_id":654,"city_id":1698,"is_default":false,"link":"","address":"\u0432\u0443\u043b.\u0420\u0443\u0441\u044c\u043a\u0430, 23","timetable":"<p>\u041f\u043e\u043d\u0435\u0434\u0456\u043b\u043e\u043a \u2013 \u041f\u2019\u044f\u0442\u043d\u0438\u0446\u044f \u0437 <strong>8<sup>00<\/sup><\/strong> \u0434\u043e <strong>21<sup>00<\/sup><\/strong><\/p>\r\n<p>\u0421\u0443\u0431\u043e\u0442\u0430,\u041d\u0435\u0434\u0456\u043b\u044f <strong>9<sup>00<\/sup><\/strong> \u0434\u043e <strong>19<sup>00<\/sup><\/strong><\/p>"},{"ext_id":440,"city_id":2531,"is_default":false,"link":"","address":"\u0432\u0443\u043b. \u041f\u0435\u0440\u0448\u043e\u0442\u0440\u0430\u0432\u043d\u0435\u0432\u0430, 53                                                               ","timetable":"<p>\u0429\u043e\u0434\u0435\u043d\u043d\u043e \u0437  <strong>8<sup>00<\/sup><\/strong> \u0434\u043e <strong>21<sup>00<\/sup><\/strong><\/p>\r\n"},{"ext_id":670,"city_id":1666,"is_default":false,"link":"","address":"\u043f\u043b\u043e\u0449\u0430 \u041f\u0440\u0438\u0432\u043e\u043a\u0437\u0430\u043b\u044c\u043d\u0430,7\/1                                                                  ","timetable":"<p>\u041f\u043e\u043d\u0435\u0434\u0456\u043b\u043e\u043a \u2013 \u041f\u2019\u044f\u0442\u043d\u0438\u0446\u044f \u0437 <strong>8<sup>00<\/sup><\/strong> \u0434\u043e <strong>21<sup>00<\/sup><\/strong><\/p>\r\n<p>\u0421\u0443\u0431\u043e\u0442\u0430 - \u041d\u0435\u0434\u0456\u043b\u044f \u0437 <strong>8<sup>00<\/sup><\/strong> \u0434\u043e <strong>20<sup>00<\/sup><\/strong><\/p>\r\n\r\n"},{"ext_id":694,"city_id":1909,"is_default":false,"link":"","address":"\u0432\u0443\u043b.\u0421\u0443\u0440\u043c\u0438\u0447\u0456, 100  ","timetable":"<p>\u041f\u043e\u043d\u0435\u0434\u0456\u043b\u043e\u043a \u2013 \u041d\u0435\u0434\u0456\u043b\u044f \u0437 <strong>8<sup>00<\/sup><\/strong> \u0434\u043e <strong>21<sup>00<\/sup><\/strong><\/p>\r\n"},{"ext_id":422,"city_id":1609,"is_default":false,"link":"","address":"\u0432\u0443\u043b.\u0426\u0435\u043d\u0442\u0440\u0430\u043b\u044c\u043d\u0430, 41\/19","timetable":"<p>\u041f\u043e\u043d\u0435\u0434\u0456\u043b\u043e\u043a \u2013 \u041f\u2019\u044f\u0442\u043d\u0438\u0446\u044f \u0437 <strong>8<sup>00<\/sup><\/strong> \u0434\u043e <strong>21<sup>00<\/sup><\/strong><\/p>\r\n<p>\u0421\u0443\u0431\u043e\u0442\u0430, \u041d\u0435\u0434\u0456\u043b\u044f \u0437 <strong>9<sup>00<\/sup><\/strong> \u0434\u043e <strong>20<sup>00<\/sup><\/strong><\/p>\r\n"},{"ext_id":696,"city_id":1718,"is_default":false,"link":"","address":"\u0432\u0443\u043b.\u0421\u0442\u0430\u0440\u043e\u043a\u043e\u043d\u0441\u0442\u044f\u043d\u0442\u0438\u043d\u0456\u0432\u0441\u044c\u043a\u0435 \u0448\u043e\u0441\u0435,17\/1                                  ","timetable":"<p>\u041f\u043e\u043d\u0435\u0434\u0456\u043b\u043e\u043a \u2013 \u0421\u0443\u0431\u043e\u0442\u0430 \u0437 <strong>8<sup>00<\/sup><\/strong> \u0434\u043e <strong>20<sup>00<\/sup><\/strong><\/p>\r\n<p>\u041d\u0435\u0434\u0456\u043b\u044f \u0437 <strong>9<sup>00<\/sup><\/strong> \u0434\u043e <strong>20<sup>00<\/sup><\/strong><\/p>"},{"ext_id":713,"city_id":2090,"is_default":false,"link":"","address":"\u0432\u0443\u043b.\u041c\u0430\u0439\u0434\u0430\u043d \u0428\u0435\u0432\u0447\u0435\u043d\u043a\u0430, 18","timetable":"<p>\u041f\u043e\u043d\u0435\u0434\u0456\u043b\u043e\u043a \u2013 \u041d\u0435\u0434\u0456\u043b\u044f \u0437 <strong>8<sup>00<\/sup><\/strong> \u0434\u043e <strong>20<sup>00<\/sup><\/strong><\/p>\r\n"},{"ext_id":675,"city_id":1698,"is_default":false,"link":"","address":"\u0432\u0443\u043b.\u041a\u0438\u0457\u0432\u0441\u044c\u043a\u0430, 18","timetable":"<p>\u041f\u043e\u043d\u0435\u0434\u0456\u043b\u043e\u043a \u2013 \u0421\u0443\u0431\u043e\u0442\u0430 \u0437 <strong>8<sup>00<\/sup><\/strong> \u0434\u043e <strong>21<sup>00<\/sup><\/strong><\/p>\r\n<p>\u041d\u0435\u0434\u0456\u043b\u044f <strong>9<sup>00<\/sup><\/strong> \u0434\u043e <strong>20<sup>00<\/sup><\/strong><\/p>"},{"ext_id":748,"city_id":2075,"is_default":false,"link":"","address":"\u0432\u0443\u043b.\u0411\u043e\u0433\u0434\u0430\u043d\u0430 \u0425\u043c\u0435\u043b\u044c\u043d\u0438\u0446\u044c\u043a\u043e\u0433\u043e, 46\u0411","timetable":"<p>\u041f\u043e\u043d\u0435\u0434\u0456\u043b\u043e\u043a \u2013 \u041f\u2019\u044f\u0442\u043d\u0438\u0446\u044f \u0437 <strong>8<sup>00<\/sup><\/strong> \u0434\u043e <strong>20<sup>00<\/sup><\/strong><\/p>\r\n<p>\u0421\u0443\u0431\u043e\u0442\u0430 - \u041d\u0435\u0434\u0456\u043b\u044f \u0437 <strong>8<sup>00<\/sup><\/strong> \u0434\u043e <strong>20<sup>00<\/sup><\/strong><\/p>\r\n"},{"ext_id":745,"city_id":1655,"is_default":false,"link":"","address":"\u043f\u043b\u043e\u0449\u0430 \u041f\u0440\u0438\u0432\u043e\u043a\u0437\u0430\u043b\u044c\u043d\u0430,42","timetable":"<p>\u041f\u043e\u043d\u0435\u0434\u0456\u043b\u043e\u043a \u2013 \u041f\u2019\u044f\u0442\u043d\u0438\u0446\u044f \u0437 <strong>8<sup>00<\/sup><\/strong> \u0434\u043e <strong>20<sup>00<\/sup><\/strong><\/p>\r\n<p>\u0421\u0443\u0431\u043e\u0442\u0430 - \u041d\u0435\u0434\u0456\u043b\u044f \u0437 <strong>8<sup>00<\/sup><\/strong> \u0434\u043e <strong>20<sup>00<\/sup><\/strong><\/p>\r\n"},{"ext_id":756,"city_id":2121,"is_default":false,"link":"","address":"\u0432\u0443\u043b.\u0421.\u0411\u0430\u043d\u0434\u0435\u0440\u0438,21\u0410","timetable":"<p>\u041f\u043e\u043d\u0435\u0434\u0456\u043b\u043e\u043a \u2013 \u041f\u2019\u044f\u0442\u043d\u0438\u0446\u044f \u0437 <strong>8<sup>00<\/sup><\/strong> \u0434\u043e <strong>20<sup>00<\/sup><\/strong><\/p>\r\n<p>\u0421\u0443\u0431\u043e\u0442\u0430 - \u041d\u0435\u0434\u0456\u043b\u044f \u0437 <strong>8<sup>00<\/sup><\/strong> \u0434\u043e <strong>20<sup>00<\/sup><\/strong><\/p>\r\n"},{"ext_id":734,"city_id":1728,"is_default":false,"link":"","address":"\u043f\u0440.\u041f\u0435\u0440\u0435\u043c\u043e\u0433\u0438, 82","timetable":"<p>\u041f\u043e\u043d\u0435\u0434\u0456\u043b\u043e\u043a \u2013 \u041f'\u044f\u0442\u043d\u0438\u0446\u044f \u0437 <strong>8<sup>00<\/sup><\/strong> \u0434\u043e <strong>21<sup>00<\/sup><\/strong><\/p>\r\n<p>\u0421\u0443\u0431\u043e\u0442\u0430 - \u041d\u0435\u0434\u0456\u043b\u044f <strong>9<sup>00<\/sup><\/strong> \u0434\u043e <strong>20<sup>00<\/sup><\/strong><\/p>"},{"ext_id":750,"city_id":1713,"is_default":false,"link":"","address":"\u0432\u0443\u043b. \u041d\u0435\u0431\u0435\u0441\u043d\u043e\u0457 \u0441\u043e\u0442\u043d\u0456, 5 ","timetable":"<p>\u041f\u043e\u043d\u0435\u0434\u0456\u043b\u043e\u043a \u0437 <strong>8<sup>00<\/sup><\/strong> \u0434\u043e <strong>21<sup>00<\/sup><\/strong><\/p>\r\n<p>\u0412\u0456\u0432\u0442\u043e\u0440\u043e\u043a \u0437 <strong>7<sup>00<\/sup><\/strong> \u0434\u043e <strong>21<sup>00<\/sup><\/strong><\/p>\r\n<p>\u0421\u0435\u0440\u0435\u0434\u0430 \u0437 <strong>8<sup>00<\/sup><\/strong> \u0434\u043e <strong>21<sup>00<\/sup><\/strong><\/p>\r\n<p>\u0427\u0435\u0442\u0432\u0435\u0440 \u0437 <strong>8<sup>00<\/sup><\/strong> \u0434\u043e <strong>21<sup>00<\/sup><\/strong><\/p>\r\n<p>\u041f'\u044f\u0442\u043d\u0438\u0446\u044f \u0437 <strong>7<sup>00<\/sup><\/strong> \u0434\u043e <strong>21<sup>00<\/sup><\/strong><\/p>\r\n<p>\u0421\u0443\u0431\u043e\u0442\u0430 \u0437 <strong>8<sup>00<\/sup><\/strong> \u0434\u043e <strong>21<sup>00<\/sup><\/strong><\/p>\r\n<p>\u041d\u0435\u0434\u0456\u043b\u044f \u0437 <strong>7<sup>00<\/sup><\/strong> \u0434\u043e <strong>21<sup>00<\/sup><\/strong><\/p>"},{"ext_id":189,"city_id":1976,"is_default":false,"link":"","address":"\u043f\u0440\u043e\u0441\u043f.\u041f\u0435\u0440\u0435\u043c\u043e\u0433\u0438, 100\u0410 ","timetable":"<p>\u041f\u041d-\u041d\u0414 \u0437  <strong>07<sup>30<\/sup><\/strong> \u0434\u043e <strong>20<sup>30<\/sup><\/strong><\/p>\r\n"},{"ext_id":99,"city_id":2088,"is_default":false,"link":"","address":"\u0432\u0443\u043b.\u041a\u043e\u0441\u043c\u043e\u043d\u0430\u0432\u0442\u0430 \u0411\u0454\u043b\u044f\u0454\u0432\u0430,9\/13 ","timetable":"<p>\u041f\u043e\u043d\u0435\u0434\u0456\u043b\u043e\u043a \u2013 \u0421\u0443\u0431\u043e\u0442\u0430 \u0437 <strong>8<sup>00<\/sup><\/strong> \u0434\u043e <strong>20<sup>00<\/sup><\/strong><\/p>\r\n<p>\u041d\u0435\u0434\u0456\u043b\u044f \u0437 <strong>9<sup>00<\/sup><\/strong> \u0434\u043e <strong>19<sup>00<\/sup><\/strong><\/p>"},{"ext_id":738,"city_id":2054,"is_default":false,"link":"","address":"\u0432\u0443\u043b.\u041b\u044e\u0431\u0456\u043d\u0441\u044c\u043a\u0430,102                                                                          ","timetable":"<p>\u041f\u043e\u043d\u0435\u0434\u0456\u043b\u043e\u043a \u2013 \u041f\u2019\u044f\u0442\u043d\u0438\u0446\u044f \u0437 <strong>7<sup>30<\/sup><\/strong> \u0434\u043e <strong>21<sup>30<\/sup><\/strong><\/p>\r\n<p>\u0421\u0443\u0431\u043e\u0442\u0430, \u041d\u0435\u0434\u0456\u043b\u044f \u0437 <strong>8<sup>00<\/sup><\/strong> \u0434\u043e <strong>20<sup>00<\/sup><\/strong><\/p>\r\n"},{"ext_id":777,"city_id":2054,"is_default":false,"link":"","address":"\u0432\u0443\u043b.\u0412\u043e\u043b\u043e\u0434\u0438\u043c\u0438\u0440\u0430 \u0412\u0435\u043b\u0438\u043a\u043e\u0433\u043e,27                                                                 ","timetable":"<p>\u0429\u043e\u0434\u0435\u043d\u043d\u043e \u0437  <strong>8<sup>00<\/sup><\/strong> \u0434\u043e <strong>21<sup>00<\/sup><\/strong><\/p>"},{"ext_id":774,"city_id":1615,"is_default":false,"link":"                                                            ","address":"\u0432\u0443\u043b.\u0411.\u0425\u043c\u0435\u043b\u044c\u043d\u0438\u0446\u044c\u043a\u043e\u0433\u043e,102    ","timetable":"<p>\u0429\u043e\u0434\u0435\u043d\u043d\u043e \u0437  <strong>8<sup>00<\/sup><\/strong> \u0434\u043e <strong>21<sup>00<\/sup><\/strong><\/p>"},{"ext_id":737,"city_id":1978,"is_default":false,"link":"","address":"\u0432\u0443\u043b. \u041f\u043e\u043f\u043e\u0432\u0430 \u043a\u043e\u0441\u043c\u043e\u043d\u0430\u0432\u0442\u0430, 9\u0430","timetable":"<p>\u041f\u043e\u043d\u0435\u0434\u0456\u043b\u043e\u043a \u2013 \u041f\u2019\u044f\u0442\u043d\u0438\u0446\u044f \u0437 <strong>07<sup>00<\/sup><\/strong> \u0434\u043e <strong>20<sup>00<\/sup><\/strong><\/p>\r\n<p>\u0421\u0443\u0431\u043e\u0442\u0430 - \u041d\u0435\u0434\u0456\u043b\u044f \u0437 <strong>8<sup>00<\/sup><\/strong> \u0434\u043e <strong>20<sup>00<\/sup><\/strong><\/p>\r\n\r\n"},{"ext_id":800,"city_id":1976,"is_default":false,"link":"","address":"\u0432\u0443\u043b.\u0413\u0435\u0440\u043e\u0457\u0432 \u0414\u043d\u0456\u043f\u0440\u0430,35","timetable":"<p>\u041f\u043e\u043d\u0435\u0434\u0456\u043b\u043e\u043a \u2013 \u041f\u2019\u044f\u0442\u043d\u0438\u0446\u044f \u0437 <strong>8<sup>00<\/sup><\/strong> \u0434\u043e <strong>21<sup>00<\/sup><\/strong><\/p>\r\n<p>\u0421\u0443\u0431\u043e\u0442\u0430,\u041d\u0435\u0434\u0456\u043b\u044f <strong>9<sup>00<\/sup><\/strong> \u0434\u043e <strong>20<sup>00<\/sup><\/strong><\/p>"},{"ext_id":791,"city_id":1924,"is_default":false,"link":"","address":"\u0432\u0443\u043b.\u0427\u0443\u043c\u0430\u0447\u0435\u043d\u043a\u0430,34                                                                       ","timetable":"<p>\u041f\u043e\u043d\u0435\u0434\u0456\u043b\u043e\u043a \u2013 \u0421\u0443\u0431\u043e\u0442\u0430 \u0437 <strong>7<sup>00<\/sup><\/strong> \u0434\u043e <strong>21<sup>00<\/sup><\/strong><\/p>\r\n<p>\u041d\u0435\u0434\u0456\u043b\u044f <strong>9<sup>00<\/sup><\/strong> \u0434\u043e <strong>20<sup>00<\/sup><\/strong><\/p>"},{"ext_id":793,"city_id":1924,"is_default":false,"link":"https:\/\/goo.gl\/kq4Jle","address":"\u043f\u0440\u043e\u0441\u043f\u0435\u043a\u0442 \u0421\u043e\u0431\u043e\u0440\u043d\u0438\u0439,109\/313                                                              ","timetable":"<p>\u041f\u043e\u043d\u0435\u0434\u0456\u043b\u043e\u043a \u2013 \u041d\u0435\u0434\u0456\u043b\u044f \u0437 <strong>8<sup>00<\/sup><\/strong> \u0434\u043e <strong>21<sup>00<\/sup><\/strong><\/p>\r\n"},{"ext_id":731,"city_id":1855,"is_default":false,"link":"","address":"\u0432\u0443\u043b.\u041d\u0435\u0437\u0430\u043b\u0435\u0436\u043d\u043e\u0441\u0442\u0456,60\/1   ","timetable":"<p>\u041f\u043e\u043d\u0435\u0434\u0456\u043b\u043e\u043a \u2013 \u0421\u0443\u0431\u043e\u0442\u0430 \u0437 <strong>8<sup>00<\/sup><\/strong> \u0434\u043e <strong>20<sup>00<\/sup><\/strong><\/p>\r\n<p>\u041d\u0435\u0434\u0456\u043b\u044f <strong>9<sup>00<\/sup><\/strong> \u0434\u043e <strong>19<sup>00<\/sup><\/strong><\/p>\r\n"},{"ext_id":810,"city_id":1946,"is_default":false,"link":"","address":"\u0432\u0443\u043b.\u0427\u043e\u0440\u043d\u043e\u0432\u043e\u043b\u0430,35\/120                                                            ","timetable":"<p>\u041f\u041d-\u041f\u0422 \u0437  <strong>08<sup>00<\/sup><\/strong> \u0434\u043e <strong>21<sup>00<\/sup><\/strong><\/p>\r\n<p>\u0421\u0411 \u0437  <strong>08<sup>00<\/sup><\/strong> \u0434\u043e <strong>20<sup>00<\/sup><\/strong><\/p>\r\n<p> \u041d\u0414 \u0437  <strong>09<sup>00<\/sup><\/strong> \u0434\u043e <strong>20<sup>00<\/sup><\/strong><\/p>"},{"ext_id":806,"city_id":1976,"is_default":false,"link":"https:\/\/goo.gl\/maps\/Lniok5MbCjv","address":" \u0432\u0443\u043b.\u042f.\u0406\u0432\u0430\u0448\u043a\u0435\u0432\u0438\u0447\u0430,4                                                                          ","timetable":"<p>\u0429\u043e\u0434\u0435\u043d\u043d\u043e \u0437  <strong>8<sup>00<\/sup><\/strong> \u0434\u043e <strong>21<sup>00<\/sup><\/strong><\/p>"},{"ext_id":548,"city_id":1896,"is_default":false,"link":"","address":"\u043f\u0440. \u042f\u0432\u043e\u0440\u043d\u0438\u0446\u044c\u043a\u043e\u0433\u043e, 123 \u043f\u0440\u0438\u043c.1","timetable":"<p>\u041f\u043e\u043d\u0435\u0434\u0456\u043b\u043e\u043a \u2013 \u041d\u0435\u0434\u0456\u043b\u044f \u0437 <strong>7<sup>00<\/sup><\/strong> \u0434\u043e <strong>21<sup>00<\/sup><\/strong><\/p>\r\n"},{"ext_id":803,"city_id":2052,"is_default":false,"link":"","address":" \u0432\u0443\u043b.\u0413\u0440\u0443\u0448\u0435\u0432\u0441\u044c\u043a\u043e\u0433\u043e,31                                                                        ","timetable":"<p>\u041f\u043e\u043d\u0435\u0434\u0456\u043b\u043e\u043a \u2013 \u0421\u0443\u0431\u043e\u0442\u0430 \u0437 <strong>8<sup>00<\/sup><\/strong> \u0434\u043e <strong>22<sup>00<\/sup><\/strong><\/p>\r\n<p>\u041d\u0435\u0434\u0456\u043b\u044f <strong>8<sup>00<\/sup><\/strong> \u0434\u043e <strong>21<sup>00<\/sup><\/strong><\/p>\r\n"},{"ext_id":808,"city_id":1978,"is_default":false,"link":"","address":" \u0432\u0443\u043b.\u0414\u043e\u0431\u0440\u043e\u0432\u043e\u043b\u044c\u0441\u044c\u043a\u043e\u0433\u043e,22\u0413                                                            ","timetable":"<p>\u041f\u043e\u043d\u0435\u0434\u0456\u043b\u043e\u043a \u2013 \u041d\u0435\u0434\u0456\u043b\u044f \u0437 <strong>7<sup>00<\/sup><\/strong> \u0434\u043e <strong>20<sup>00<\/sup><\/strong><\/p>\r\n"},{"ext_id":828,"city_id":1963,"is_default":false,"link":"","address":"\u043f\u0440. \u041b\u0435\u0441\u0456 \u0423\u043a\u0440\u0430\u0457\u043d\u043a\u0438, 15\u0410\/174                                                            ","timetable":"<p>\u041f\u043d-\u0421\u0431 \u0437  <strong>8<sup>00<\/sup><\/strong> \u0434\u043e <strong>20<sup>00<\/sup><\/strong><\/p>\r\n<p>\u041d\u0434 \u0437  <strong>9<sup>00<\/sup><\/strong> \u0434\u043e <strong>19<sup>00<\/sup><\/strong><\/p>"},{"ext_id":839,"city_id":1727,"is_default":false,"link":"","address":"\u0432\u0443\u043b. \u0421\u0443\u043c\u0433\u0430\u0457\u0442\u0441\u044c\u043a\u0430, 39                                                                    ","timetable":"<p>\u041f\u043e\u043d\u0435\u0434\u0456\u043b\u043e\u043a \u2013 \u041d\u0435\u0434\u0456\u043b\u044f \u0437 <strong>8<sup>00<\/sup><\/strong> \u0434\u043e <strong>21<sup>00<\/sup><\/strong><\/p>\r\n"},{"ext_id":836,"city_id":1793,"is_default":false,"link":"https:\/\/goo.gl\/maps\/Lniok5MbCjv","address":" \u0432\u0443\u043b. \u0421. \u0411\u0430\u043d\u0434\u0435\u0440\u0438, 12\/2                                                                  ","timetable":"<p>\u0429\u043e\u0434\u0435\u043d\u043d\u043e \u0437  <strong><sup>30<\/sup><\/strong> \u0434\u043e <strong>20<sup>00<\/sup><\/strong><\/p>"},{"ext_id":843,"city_id":1698,"is_default":false,"link":"https:\/\/goo.gl\/maps\/Lniok5MbCjv","address":"\u0432\u0443\u043b.\u0427\u043e\u0440\u043d\u043e\u0432\u043e\u043b\u0430 \u0412`\u044f\u0447\u0435\u0441\u043b\u0430\u0432\u0430, 17\/16                                                         ","timetable":"<p>\u0429\u043e\u0434\u0435\u043d\u043d\u043e \u0437  <strong>8<sup>00<\/sup><\/strong> \u0434\u043e <strong>21<sup>00<\/sup><\/strong><\/p>"},{"ext_id":834,"city_id":2070,"is_default":false,"link":"https:\/\/goo.gl\/maps\/Lniok5MbCjv","address":"\u043f\u0440\u043e\u0441\u043f\u0435\u043a\u0442 \u041c\u0435\u0442\u0430\u043b\u0443\u0440\u0433\u0456\u0432,180                                                                 ","timetable":"<p>\u0429\u043e\u0434\u0435\u043d\u043d\u043e \u0437  <strong>8<sup>00<\/sup><\/strong> \u0434\u043e <strong>21<sup>00<\/sup><\/strong><\/p>"},{"ext_id":528,"city_id":2054,"is_default":false,"link":"https:\/\/goo.gl\/maps\/XLwaW54V2Rn","address":"\u0432\u0443\u043b.\u0412.\u0427\u043e\u0440\u043d\u043e\u0432\u043e\u043b\u0430,45                                                                         ","timetable":"<p>\u041f\u043e\u043d\u0435\u0434\u0456\u043b\u043e\u043a \u2013 \u041f\u2019\u044f\u0442\u043d\u0438\u0446\u044f \u0437 <strong>8<sup>00<\/sup><\/strong> \u0434\u043e <strong>22<sup>00<\/sup><\/strong><\/p>\r\n<p>\u0421\u0443\u0431\u043e\u0442\u0430 \u0437 <strong>8<sup>00<\/sup><\/strong> \u0434\u043e <strong>20<sup>00<\/sup><\/strong><\/p>\r\n<p>\u041d\u0435\u0434\u0456\u043b\u044f \u0437 <strong>9<sup>00<\/sup><\/strong> \u0434\u043e <strong>19<sup>00<\/sup><\/strong><\/p>"},{"ext_id":833,"city_id":1727,"is_default":false,"link":"https:\/\/goo.gl\/maps\/Lniok5MbCjv","address":"\u0432\u0443\u043b.\u041a\u0456\u0448\u043a\u0438 \u0421\u0430\u043c\u0456\u0439\u043b\u0430, 216                                                                    ","timetable":"<p>\u0429\u043e\u0434\u0435\u043d\u043d\u043e \u0437  <strong>8<sup>00<\/sup><\/strong> \u0434\u043e <strong>21<sup>00<\/sup><\/strong><\/p>"},{"ext_id":845,"city_id":2448,"is_default":false,"link":"https:\/\/goo.gl\/maps\/Lniok5MbCjv","address":"\u0432\u0443\u043b. \u0428\u0438\u0440\u043e\u043a\u0430, 64 (\u041b\u0435\u0432\u0430\u043d\u0434\u0456\u0432\u043a\u0430)","timetable":"<p>\u0429\u043e\u0434\u0435\u043d\u043d\u043e \u0437  <strong>8<sup>00<\/sup><\/strong> \u0434\u043e <strong>21<sup>00<\/sup><\/strong><\/p>"},{"ext_id":570,"city_id":1727,"is_default":false,"link":"https:\/\/goo.gl\/maps\/Lniok5MbCjv","address":"\u0432\u0443\u043b.\u0412\u0435\u0440\u043d\u0438\u0433\u043e\u0440\u0438, 4                                                                         ","timetable":"<p>\u0429\u043e\u0434\u0435\u043d\u043d\u043e \u0437  <strong>8<sup>00<\/sup><\/strong> \u0434\u043e <strong>21<sup>00<\/sup><\/strong><\/p>"},{"ext_id":848,"city_id":1716,"is_default":false,"link":"https:\/\/goo.gl\/maps\/Lniok5MbCjv","address":"\u0432\u0443\u043b. \u0414\u0435\u0440\u0435\u0432`\u044f\u043d\u043a\u0430 58                                                                       ","timetable":"<p>\u0429\u043e\u0434\u0435\u043d\u043d\u043e \u0437  <strong>8<sup>00<\/sup><\/strong> \u0434\u043e <strong>21<sup>00<\/sup><\/strong><\/p>"},{"ext_id":860,"city_id":1946,"is_default":false,"link":"","address":"\u043f\u0440\u043e\u0441\u043f. \u041d\u0435\u0437\u0430\u043b\u0435\u0436\u043d\u043e\u0441\u0442\u0456 36","timetable":"<p>\u041f\u043d-\u041d\u0434 \u0437  <strong>8<sup>00<\/sup><\/strong> \u0434\u043e <strong>21<sup>00<\/sup><\/strong><\/p>\r\n"},{"ext_id":856,"city_id":2088,"is_default":false,"link":"","address":"\u0432\u0443\u043b.\u041f\u0438\u0440\u043e\u0433\u043e\u0432\u0430 \u041c\u0438\u043a\u043e\u043b\u0438 11\/2","timetable":"<p>\u041f\u043e\u043d\u0435\u0434\u0456\u043b\u043e\u043a \u2013 \u041f\u2019\u044f\u0442\u043d\u0438\u0446\u044f \u0437 <strong>8<sup>00<\/sup><\/strong> \u0434\u043e <strong>22<sup>00<\/sup><\/strong><\/p>\r\n<p>\u0421\u0443\u0431\u043e\u0442\u0430 \u0437 <strong>8<sup>00<\/sup><\/strong> \u0434\u043e <strong>19<sup>00<\/sup><\/strong><\/p>\r\n<p>\u041d\u0435\u0434\u0456\u043b\u044f \u0437 <strong>8<sup>00<\/sup><\/strong> \u0434\u043e <strong>19<sup>00<\/sup><\/strong><\/p>"},{"ext_id":858,"city_id":1924,"is_default":false,"link":"https:\/\/goo.gl\/maps\/Lniok5MbCjv","address":" \u0432\u0443\u043b. \u0415\u043d\u0442\u0443\u0437\u0456\u0430\u0441\u0442\u0456\u0432 2                                                                    ","timetable":"<p>\u0429\u043e\u0434\u0435\u043d\u043d\u043e \u0437  <strong>8<sup>00<\/sup><\/strong> \u0434\u043e <strong>21<sup>00<\/sup><\/strong><\/p>"},{"ext_id":865,"city_id":1729,"is_default":false,"link":"https:\/\/goo.gl\/maps\/Lniok5MbCjv","address":" \u0432\u0443\u043b. \u0413\u0435\u0440\u043e\u0457\u0432 \u041c\u0430\u0439\u0434\u0430\u043d\u0443 27                                                                 ","timetable":"<p>\u0429\u043e\u0434\u0435\u043d\u043d\u043e \u0437  <strong>8<sup>00<\/sup><\/strong> \u0434\u043e <strong>21<sup>00<\/sup><\/strong><\/p>"}]),
        cookieOptions = {domain: cookieDomain, path: cookiePath};

    document.addEventListener('DOMContentLoaded', function(){
			RegExp.escape= function(s) {
		return s.replace(/[-\/\\^$*+?.()|[\]{}]/g, '\\$&');
	};	
	if($.cookie('warehouse_id')){
		$.ui.autocomplete.prototype._renderItem = function(ul, item) {
			var query = this.term.trim();
			query.replace(/\s+/, ' ');
			var words = query.split(' ');
			var label = item.label;
			$.each(words, function(i, word) {
				var re = new RegExp(RegExp.escape(word), 'gi') ;
				label = label.replace(re, '<strong>' + word + '</strong>');
			});
			return $('<li></li>')
				.data('item.autocomplete', item)
				.append('<div>' + label + '</div>')
				.appendTo(ul);
		};

		// Refactoring: changed $.getJSON to $.ajax, because in IE 11 request wasn't transformed to utf-8 charset automatically
		$('#query').autocomplete({
			source: function (request, response) {
				$.ajax({
					url:"/autocomplete.json?query=" + request.term,
					contentType: "application/json; charset=utf-8",
					data: {query:request.term},
					success: function (data) {
						response($.map(data.results, function (value) {
							return {
								label: value.name,
								value: value.name,
								ext_id: value.id
							};
						}));
					}
				});
			},
			minLength: 2,
			select: function (event, ui) {
				$('#query').val(ui.item.value);
				$('#ext_id').val(ui.item.ext_id);
				$('#search-form').submit();
			}
		});
	} else {		
		$('#query').attr('autocomplete', 'off');
	}
	$('#search-form').submit(function() {
		startProcess();
		return true;
	});
	initPopup({
		buttonSelector: '#btn-timetable',
		contentSelector: 'timetable'
	});
	initPopup({
		buttonSelector: '#btn-warehouse',
		contentSelector: 'warehouse',
		onOpen: initWarehouseSelector,
        closable: !$.cookie('warehouse_id') ? false : true
	});
    initPopup({
        buttonSelector: '#btn-city',
        contentSelector: 'city',
        onOpen: initCitySelector,
        closable: !$.cookie('warehouse_id') ? false : true
    });
    $('#btn-city-select').click(function(e) {
        e.preventDefault();
        if (!$(this).hasClass('btn-disabled')) {
            if ($.cookie('city_id') == 0) {
                setWarehouse(Warehouses.getDefault().ext_id);
            }
            else {
                $('#btn-warehouse').trigger('click');
                initWarehousePopup();
            }
        }
    });
    initPopup({
        buttonSelector: '#cant-add-to-cart',
        contentSelector: 'cant-add-to-cart'
    });
	initPopup({
		buttonSelector: '#btn-added-to-cart',
		contentSelector: 'added-to-cart',
        popupClass: 'popup-added-to-cart'
	});
	initPopup({
		buttonSelector: '#btn-auth',
		contentSelector: 'auth',
		onOpen: function() {
			$('#auth-block').removeClass('hidden');
			$('#remind-block').addClass('hidden');
			$('#password-block').addClass('hidden');
			$('.auth-wrapper .field-error').addClass('hidden');
			Inputmask({mask: '+38 (999) 999-99-99'}).mask('#login-phone');
			Inputmask({mask: '+38 (999) 999-99-99'}).mask('#remind-phone');
			$('#link-remind').unbind('click').click(function(e){
				e.preventDefault();
				$('#remind-phone').val($('#login-phone').val());
				$('#auth-block').addClass('hidden');
				$('#remind-block').removeClass('hidden');
			});
			$('#link-auth').unbind('click').click(function(e){
				e.preventDefault();
				$('#remind-block').addClass('hidden');
				$('#auth-block').removeClass('hidden');
			});
			$('#link-remind-back').unbind('click').click(function(e){
				e.preventDefault();
				$('#remind-phone').val('');
				$('#password-block').addClass('hidden');
				$('#remind-block').removeClass('hidden');
			});
			$('#link-send-again').unbind('click').click(function(e){
				e.preventDefault();
				$('#password-block').addClass('hidden');
				$('#remind-block').removeClass('hidden');
			});
			$('#auth-form').unbind('submit').submit(function(){
				startProcess();
				$('#auth-form').removeClass('error');
				$('#auth-form .field-error').addClass('hidden');
				$.ajax({
					url: $(this).attr('action'),
					type: 'post',
					data: $(this).serialize(),
					dataType: 'json',
					success: function(data) {
						if (data.success) {
							window.location.reload();
						}
						else {
							$('#auth-form').addClass('error');
							$('#auth-form .field-error').removeClass('hidden');
							stopProcess();
						}
					},
					error: stopProcess
				});
				return false;
			});
			$('#remind-form').unbind('submit').submit(function(){
				startProcess();
				$('#remind-form').removeClass('error');
				$('.auth-wrapper .field-error').addClass('hidden');
				$.ajax({
					url: $(this).attr('action'),
					type: 'post',
					data: $(this).serialize(),
					dataType: 'json',
					success: function(data) {
						stopProcess();
						if (data.success) {
							$('#sent-phone').html($('#remind-phone').val());
							$('#change-password-phone').val($('#remind-phone').val());
							$('#remind-block').addClass('hidden');
							$('#password-block').removeClass('hidden');
						}
						else {
							$('#remind-form').addClass('error');
							$('#error-remind').removeClass('hidden').html(data.error);
						}
					},
					error: stopProcess
				});
				return false;
			});
			$('#password-form').unbind('submit').submit(function(){
				startProcess();
				$('#password-form').removeClass('error');
				$('.auth-wrapper .field-error').addClass('hidden');
				$.ajax({
					url: $(this).attr('action'),
					type: 'post',
					data: $(this).serialize(),
					dataType: 'json',
					success: function(data) {
						stopProcess();
						if (data.success) {
							$('#password-block').addClass('hidden');
							$('#auth-block').removeClass('hidden');
						}
						else {
							$('#password-form').addClass('error');
							for (key in data.errors) {
								for (error_code in data.errors[key]) {
									$('#error-' + key).removeClass('hidden').html(data.errors[key][error_code]);
								}
							}
						}
					},
					error: stopProcess
				});
				return false;
			});
		}
	});
	var openedAnalogue = 0,
		currentMainRowClass,
		headerHeight = $('.search-results-wrapper > header').height();

	$('.search-results-wrapper.scroll-wrapper .results-scrollable-wrapper').css('padding-top', headerHeight);

	function checkScroll() {
		console.log(headerHeight);
		$('.thead-wrapper .inner-wrapper table tbody tr:not(:first-child)').each(function(){
			var currentHeaderMainRowDataClass = $(this).attr('data-class');
			$('.mainrow.visible').each(function(){
				var currentDataClass = $(this).attr('data-class');
				if ( $(this).offset().top < headerHeight && $(this).attr('data-class') == $('.thead-wrapper .inner-wrapper table tbody tr.' + currentDataClass).attr('data-class') ) {
					$('.thead-wrapper .inner-wrapper table tbody tr.' + currentDataClass).removeClass('hidden');
				}
				else {
					$('.thead-wrapper .inner-wrapper table tbody tr.' + currentDataClass).addClass('hidden');
				}
				if ( $(this).next().find('tr:last-child').offset().top < headerHeight && $(this).next().attr('data-class') == $('.thead-wrapper .inner-wrapper table tbody tr.' + currentDataClass).attr('data-class') ) {
					$('.thead-wrapper .inner-wrapper table tbody tr.' + currentDataClass).addClass('hidden');
				}
			})
		})
	};
	function ShowOrHideScroll(){
		if ( $(window).width() > 1024 ) {
			$('.results-scrollable-wrapper .content-wrapper').mCustomScrollbar({
				scrollInertia: 100,
				callbacks:{
					whileScrolling: function() {
						if (this.mcs.top < 0) {
							$('header').addClass('fixed');
						}
						else {
							$('header').removeClass('fixed');
						}
						if (openedAnalogue > 0) {
							checkScroll();
						}
					}
				}
			});
		}
		else {
			$('.scroll-wrapper .content-wrapper').on('scroll', function(){
				if (openedAnalogue > 0) {
					checkScroll();
				}	
			});
		}
	};

	ShowOrHideScroll();

	$(window).resize(function(){
		ShowOrHideScroll();
	});

	var fixedElem = $('.search-results-wrapper header');

	$(fixedElem).on('touchmove', function(e) {
	        e.preventDefault();
	        console.log('prvntDflt');
	}, false);

	$('.item-similar a').click(function(e) {
		var ext_id = $(this).data('id'),
			closest_tbody = $(this).closest('tbody'),
			currentMainCloneRow;
		if ($(this).hasClass('active')) {
			$(this).removeClass('active');
			$(this).html('<i class="icon-arrow-down"></i>дивитись аналоги товару');
			$(this).parents('tbody').next().hide();
			closest_tbody.removeClass('visible');
			closest_tbody.next().removeClass('visible').addClass('hidden');
			openedAnalogue --;
		}
		else {
			$(this).addClass('active');
			$(this).html('<i class="icon-arrow-up"></i>приховати аналоги товару');
			$(this).parents('tbody').next().show();
			closest_tbody.addClass('mainrow visible');
			closest_tbody.attr('data-class', ext_id);
			closest_tbody.next().addClass('analogue visible');
			closest_tbody.next().attr('data-class', ext_id);
			openedAnalogue ++;
		}
		currentMainRowClass = $(this).data('id');
		currentMainCloneRow = $(this).closest('tr').clone(true);

		if (!$('.thead-wrapper .inner-wrapper table tbody tr').hasClass(currentMainRowClass)) {
			currentMainCloneRow.appendTo('.thead-wrapper .inner-wrapper table tbody').addClass('' + currentMainRowClass + ' hidden').attr('data-class', currentMainRowClass);
		}
		return false;
	});

	$('.item-title a').fancybox();
	$('.btn-add-to-cart').click(function(e) {
		e.preventDefault();
		var ext_id = $(this).data('id'),
			title = $(this).data('title'),
			buy_limit = $(this).data('limit');
		if(buy_limit == 0){
			startProcess();
			$.ajax({
				url: '/checkout/add',
				type: 'post',
				data: {ext_id: ext_id},
				dataType: 'json',
				success: function(data) {
					$('.btn-add-to-cart[data-id="' + ext_id + '"]').html('В кошику');
					refreshCart(data, ext_id);
					stopProcess();
					$('#btn-added-to-cart').trigger('click');
				},
				error: stopProcess
			});
		} else {
			stopProcess();
			$('.cant-add-to-cart').html(title);
			$('#cant-add-to-cart').trigger('click');
		}
	});

	initPopup({
		buttonSelector: '.btn-contract',
		contentSelector: 'contract',
		popupClass: 'popup-wide'
	});
	});
//-->
</script>
<script type="text/javascript">
/* <![CDATA[ */
var google_conversion_id = 983394014;
var google_custom_params = window.google_tag_params;
var google_remarketing_only = true;
/* ]]> */
</script>
<script type="text/javascript" src="//www.googleadservices.com/pagead/conversion.js">
</script>
<noscript>
<div style="display:inline;">
<img height="1" width="1" style="border-style:none;" alt="" src="//googleads.g.doubleclick.net/pagead/viewthroughconversion/983394014/?guid=ON&amp;script=0"/>
</div>
</noscript></body>
</html>

"""