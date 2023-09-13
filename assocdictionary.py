# assoc dictionary
import requests
import urllib.parse
import json
import aisocketapi
import os
import os.path
import database
import api
import constants

totaldict = {}
failed = []


totaldict = {}

freq = ['的','是','不','我','一','有','大','在','人','了','中','到','資','要','以','可','這','個','你','會','好','為','上','來','學','就','交','也','用','能','如','時','文','說','沒','他','看','那','問','生','提','下','過','請','們','天','所','多','麼','小','之','想','得','工','出','還','電','對','都','機','自','而','子','後','訊','家','站','心','只','去','知','國','很','台','成','信','同','何','章','道','發','地','法','無','然','但','當','於','嗎','本','年','現','前','最','真','新','和','因','果','意','定','點','情','其','題','事','科','方','些','清','三','樣','此','吧','位','作','理','行','者','經','名','什','謝','日','正','開','話','與','實','愛','再','華','二','城','動','比','面','高','又','或','力','應','女','種','教','車','分','像','系','長','手','次','已','明','打','太','路','起','己','相','主','關','十','間','鳳','外','呢','覺','使','該','友','才','進','凰','她','民','著','各','全','將','少','兩','加','回','感','式','第','球','性','老','程','把','被','公','論','及','龍','校','別','體','重','給','聽','水','做','常','您','見','裡','東','風','解','灣','月','等','啦','部','原','美','先','音','通','管','網','區','期','錯','否','樂','入','找','書','讓','四','啊','由','選','較','數','表','內','場','它','從','快','歡','至','立','目','社','合','望','怎','認','告','更','幾','考','度','難','版','頭','喜','許','光','今','買','算','弟','若','統','身','記','代','號','處','完','接','計','言','字','師','並','政','玩','張','男','誰','山','每','結','且','星','非','建','改','連','放','哈','活','研','直','設','陳','報','轉','黨','指','五','變','氣','西','試','希','神','取','化','物','王','任','林','單','世','受','近','義','死','便','反','士','戰','空','隊','跟','卻','北','必','業','功','寫','影','聲','平','臺','員','金','討','色','則','容','檔','片','向','妳','市','利','興','白','強','安','央','特','議','辦','價','總','傳','思','花','元','叫','保','份','求','究','呵','件','未','決','組','萬','竹','級','持','笑','投','哪','室','曾','走','喔','標','流','支','獨','貓','卡','需','兄','門','共','語','海','口','阿','線','馬','黃','參','般','命','視','觀','聯','腦','朋','格','兒','八','修','料','錢','失','吃','住','即','另','錄','專','象','換','基','板','拿','遠','速','形','孩','備','歌','幫','確','候','除','界','裝','類','講','器','南','案','畫','英','訴','帶','差','乎','量','久','掉','似','整','引','班','迷','圖','制','費','賽','奇','識','型','超','邊','耶','品','舍','雖','始','運','李','務','權','驗','故','六','讀','怪','飛','滿','服','夢','收','眼','造','念','留','課','軍','破','精','半','約','願','令','底','答','演','達','雄','深','票','早','院','夠','曲','假','談','術','棒','賣','黑','百','勝','推','存','火','準','示','往','碟','易','況','晚','離','治','導','七','段','團','調','證','列','傷','永','剛','排','哥','德','九','甚','殺','照','軟','包','怕','條','夜','商','概','根','供','絕','千','客','切','集','稱','據','落','越','竟','盡','待','聞','園','忘','值','產','消','雙','紅','座','展','育','跑','附','嘛','執','唱','技','某','硬','斯','雲','遊','息','助','須','苦','介','效','首','質','例','唉','職','復','輸','節','規','注','畢','查','熱','油','館','態','停','福','救','倒','親','害','亂','古','步','寶','擊','舉','終','嗯','印','限','依','斷','輕','環','簡','趣','志','響','隨','練','續','魚','篇','司','局','送','極','角','省','源','陽','幹','習','羅','武','免','疑','拉','克','仍','樓','佛','足','低','廣','煩','鳥','顯','碼','土','率','聖','壞','初','具','預','呀','眾','責','爭','兵','智','誤','境','青','順','野','楚','貴','負','壓','史','適','係','測','懷','迎','配','魔','慢','哇','懂','嗚','亦','味','評','舞','細','醫','帝','屬','句','戀','敗','宜','楊','甲','追','灌','春','左','敢','靈','狂','際','群','族','木','騎','里','項','戲','遇','狗','佳','博','右','痛','營','妹','康','善','徵','歷','官','爾','按','編','病','護','補','擇','抓','石','歲','隻','領','尋','溫','養','止','守','君','血','田','雨','居','謂','異','優','跳','拜','爛','封','惡','良','模','狀','浪','聊','增','核','激','維','陸','吳','牛','忙','詞','劇','宿','急','啥','抱','靜','攻','亞','江','致','陣','嚴','宗','警','壘','夫','密','睡','午','店','勢','悲','蘭','幕','緣','週','廠','簽','坐','香','爽','控','微','登','翻','普','蠻','冷','威','毒','俊','絡','輯','母','創','堂','趙','套','舊','雜','周','述','恐','幸','亮','麗','巴','禮','酒','仁','餐','牌','突','腳','劍','招','吉','父','仔','典','搞','房','素','防','授','充','草','暴','慮','紹','背','劉','委','府','景','憶','尤','諸','缺','援','漫','琴','罵','純','尚','藝','惜','置','益','姐','誠','繼','湖','欲','麻','靠','肉','松','刻','紀','退','既','含','判','釋','皮','波','承','射','堆','莫','製','鍵','趕','旁','筆','扁','註','奏','樹','律','鐵','榮','昨','毛','彩','歸','虎','罪','皆','葉','售','彈','衛','施','銘','刀','塊','漢','欣','布','賞','載','險','播','升','鐘','寄','弄','付','構','囉','磁','螢','偉','薦','洋','嘿','啟','梅','策','嘻','燈','鬼','檢','宣','哦','媽','均','派','豬','濟','架','享','呆','訓','藍','劃','擔','努','郭','歉','紙','貼','暗','呼','罷','巧','慧','穿','詳','雷','協','督','顧','臉','逢','島','獎','游','批','略','短','幻','沙','散','敵','鄉','冊','輪','朝','窗','忍','河','藏','衝','混','唯','乾','冠','熟','鷹','蛋','尊','棄','敬','季','婚','縣','緊','伯','申','衣','購','僅','帳','層','秋','猜','偏','鏡','食','喝','偷','贊','犯','勇','顆','姓','束','淡','詩','嘉','曉','借','徒','洲','擁','序','慶','績','祝','獅','圍','餘','私','鬥','柔','漂','富','秀','範','避','輝','譯','孤','笨','括','吸','端','移','廳','蓋','末','察','抗','揮','乖','積','插','驚','蔡','忠','愈','雪','巨','碩','瑞','凡','朱','籃','丟','盤','偶','港','宮','帥','宏','雅','貨','醒','虛','遺','掛','透','爆','烈','滅','材','拍','休','誌','圓','銀','互','飯','掌','豪','替','挑','頂','熊','累','址','健','俠','雞','困','諾','輔','伴','玉','洗','敏','臨','街','降','唸','憐','蘇','米','減','操','瘋','辛','宇','聚','兮','彼','採','屆','尼','輩','藥','騙','綠','童','縮','符','獲','默','郎','碰','禁','婆','咧','股','抽','砍','恨','肯','刊','泡','漸','鋼','廢','淚','樞','贏','歐','財','訂','途','觸','賢','傑','脫','箱','佈','仙','冰','析','蒼','厭','籍','堅','哭','夏','懶','橋','穩','露','詢','森','絲','塵','慣','濤','誼','佔','茶','賴','階','豐','貝','暑','郵','危','寒','械','隱','爸','汽','慘','旅','村','予','振','亡','瓶','遭','哲','零','納','珍','乃','席','哩','鄭','吹','骨','煙','胡','倫','洪','搖','娘','芳','索','峰','織','惠','杯','浮','狼','隔','椰','租','尾','忽','複','莊','款','菜','副','企','折','擾','揚','鼠','冒','癡','鼓','刺','頻','喵','針','霸','暫','伊','沉','嘴','庫','悔','陰','寂','倚','探','祖','摩','距','剩','遍','蟲','燒','頁','隆','弱','豆','延','蕭','握','寧','昭','盟','覆','憲','秘','耐','愁','丁','撥','沈','昇','髮','哀','龜','眉','固','卷','顏','閒','稍','殘','搭','京','傻','耳','映','託','恩','鴻','妙','辯','媒','吵','擬','違','憂','桌','拼','銷','藉','胖','屋','域','船','勞','洞','寢','井','徐','川','奈','戶','乘','額','倍','農','擺','塞','橫','賀','皇','拖','怨','牙','齊','逃','障','賺','滾','干','譜','烏','瞭','戴','搬','鬆','瓜','迫','嚇','奶','棋','鬧','盛','摸','尺','伙','染','佩','床','酷','孫','牠','屁','醉','震','鎖','凱','損','潮','役','泰','伍','冬','桃','聰','乙','迴','競','崇','撞','厲','淨','牽','羊','惑','溪','帽','眠','巷','溝','俗','宋','飄','淺','獻','麵','艦','滑','榜','圈','庭','縱','閃','蓮','麥','邦','耀','旋','閱','諒','紫','攝','儀','妨','審','描','洽','毀','逐','陪','填','踏','跌','藤','慕','勒','闆','殊','姊','憑','寞','岸','芬','鎮','池','拒','葛','州','鋒','寬','拳','于','函','驅','后','裁','蟹','阻','邪','革','頗','臥','昌','孟','航','遙','翔','蠍','恭','奧','齋','睛','槍','塔','閉','頓','糊','仰','旗','勵','厚','魂','准','丸','宙','逸','裕','舒','訪','兼','薩','飲','赤','閣','庸','啪','搶','勿','砂','緒','丌','穹','儘','掃','慈','欄','嘗','勸','鮮','奮','賜','菩','喊','闡','幽','擴','污','彰','毫','祥','盜','証','罰','番','尖','灰','狐','衡','擎','汪','監','籌','遲','誇','邱','稅','浩','拆','紛','吾','托','姑','咱','漏','誕','淑','鬱','砲','柏','牆','窩','傾','辭','秒','羽','渡','沖','廖','輛','齡','培','邀','甘','袋','杜','酸','胸','邏','豈','涼','肥','谷','獸','娃','孔','陷','估','妻','徑','玫','潛','晶','胞','煞','脆','抹','猶','築','呂','碎','噴','截','旦','婦','垃','荒','幣','圾','串','壯','伸','傲','弦','泥','繁','魯','忌','億','叭','坦','恥','蜜','欺','捨','怡','玲','臭','唐','湯','窮','悉','勁','拔','甜','蒙','逛','朵','摘','膽','糟','腿','喇','醜','躍','繳','泉','澤','碧','鞋','韓','彥','晨','莉','駕','猛','緩','坡','炸','怒','召','捕','幼','艾','恆','割','扯','盾','么','吐','昏','辨','軒','巫','丹','鑑','彎','賦','坪','侵','胎','悠','薪','刪','彬','悟','珠','勤','瑰','植','痴','礙','敝','盃','盼','亨','逝','剪','磨','逼','濃','洛','乏','擋','姆','症','嫌','躲','壁','釣','暖','憾','遜','愉','曰','采','捷','嘆','玄','滴','扣','抵','奔','翁','蹟','菲','爬','棚','夕','惱','戒','牲','泳','恰','滄','桑','蔣','潔','焦','勉','奪','萊','咖','貪','踢','抄','跡','鍾','涯','箭','誓','穌','涉','稿','署','療','礎','僑','涵','霧','粉','俱','徹','謀','屠','犧','唷','繞','壽','爺','騷','氏','翼','云','肚','吝','梁','咪','繪','廉','飽','鳴','貌','霹','炮','捐','啡','炎','嗨','貢','曼','壢','鼻','奉','鈴','耗','恢','融','筋','撿','儒','飾','禍','侯','唬','挖','幅','瞧','廷','咦','撐','柳','薄','黎','捲','嵐','吊','靂','擠','覽','迪','凌','茫','燃','瑪','弘','矛','敦','瑜','錦','楓','賓','梯','琪','獄','側','咬','墨','悶','晴','怖','喬','齒','嶺','仲','韻','旭','綜','兔','蹤','姿','邁','傢','譽','褲','孝','促','駛','仇','粗','妮','牧','舟','糕','殼','蝶','兇','鍋','懼','銳','吟','虧','枝','耍','闊','疼','拾','毅','刷','塗','夾','裂','陀','哉','鄰','悅','契','轟','爵','屏','駐','賭','蜂','扇','羞','瓦','疏','欽','斗','坤','堪','洩','逆','抬','哎','餅','彌','貫','綱','惹','翹','墮','狠','頑','莎','擦','贈','凝','滋','靖','喂','允','彭','挺','拋','愚','征','辱','朗','余','慰','禪','蛙','秦','災','偵','讚','椅','夥','碗','丙','卒','荷','披','趨','劫','迅','笛','烤','肩','矣','遷','汝','鹿','缸','慾','爐','魅','丈','巡','措','秤','沿','痕','濫','漲','腰','賤','妥','液','鵝','軌','叔','陵','貞','扭','漠','祕','蝦','捉','謠','氛','膠','遞','霖','雯','髒','倆','旺','杉','燕','寸','茂','循','屍','鑽','晃','悄','翅','芒','斜','廁','呦','溜','鶴','喪','盒','摔','愧','灑','津','盈','脈','苗','堡','刑','叉','撒','虫','纏','遵','臣','櫻','扮','渾','噁','趁','呈','牢','泊','欠','慎','琳','倦','腐','蛇','搜','患','伏','陶','柯','劣','疲','儲','桿','祂','塑','蓉','繫','疾','泣','粒','渴','璃','茲','鄧','歪','棟','騰','玻','娟','叡','返','併','弊','埋','晉','稀','鴨','汗','牡','暢','添','妖','劑','泛','柴','杰','攜','飆','壇','阮','匆','喚','昆','拷','儂','斥','垂','萍','勾','催','糖','澎','踩','櫃','蟻','販','抑','虹','潘','坑','曹','暮','腹','煮','襲','仿','臂','吻','浴','框','敲','佑','体','彷','謹','岳','敘','賊','罐','寡','燦','侶','攤','芭','翠','羨','占','綿','謎','掩','喻','秩','煌','賠','籤','珊','馨','札','脅','旨','拘','紐','喲','蠢','詠','匙','羯','攔','膚','驟','嫁','廟','孕','俄','肝','罩','腸','叛','匪','倉','卸','祭','袍','謊','埔','几','貿','魏','禦','踴','蘋','卜','澄','麟','宵','陌','陋','屈','衷','崗','盪','曆','惟','舌','匯','誘','桂','娜','菁','睹','殿','傅','咒','謙','雀','粽','卓','鑰','斌','袖','鈕','媚','叮','翰','堯','盧','捧','壹','憤','猴','粹','跨','螞','埃','枉','卿','撕','紋','瑋','划','囂','雕','乳','膀','仗','赫','筒','辜','桶','彿','衰','獵','譬','勳','衫','懇','瓊','凍','戚','穎','軸','殖','撤','吋','寮','潭','姻','躺','樑','昂','潑','腔','龐','澳','瞬','寺','銅','閩','肢','糾','叢','卑','拓','宰','鍊','湊','梭','董','宅','刮','胃','芝','淋','斃','驕','奸','殷','墓','償','冥','炒','潤','蕩','妄','砸','餓','扎','佇','尿','眷','濕','盲','偽','踐','淫','鼎','貧','謬','矩','蟑','駁','兆','淵','棍','馳','熙','扶','聘','斬','穴','槽','詭','昧','澡','螂','辣','匹','蚊','僧','柱','挫','袁','籠','抖','訝','勃','顛','淘','撲','丘','吞','亭','瘟','癢','肆','漆','詗','尹','猩','帖','佐','昱','咳','祈','詹','毋','矮','苑','賄','緻','婉','斤','饒','闖','戈','歧','諷','熬','診','霜','諧','掙','鈞','覓','瀟','屑','痞','鋪','黏','遣','蹈','懸','詮','岡','蝴','汁','攏','帆','壺','瑟','雁','辰','婷','穗','慨','哼','淒','佬','膜','肅','濾','涂','范','恕','醬','纖','輻','懿','稚','郁','募','豫','艇','枯','掰','寵','遨','并','漁','淹','岩','墊','鞭','縫','駿','歹','斑','甄','竿','駝','昔','崎','冤','棵','僕','疊','箏','剎','墜','遮','螺','煎','薰','癮','蠟','瞎','禱','皓','坎','蒂','焉','魁','唇','犬','弓','錶','籲','娛','甩','颱','屎','沾','撫','傘','嬌','錫','唔','郝','禿','淪','剝','揭','溶','肇','匿','趟','盆','湧','坊','碳','赴','絃','磚','栗','狹','廿','菊','嘎','瘦','奴','氧','頹','璋','驢','畏','珮','債','摧','鹽','噹','噓','挽','墾','霞','伐','畔','韋','姬','逍','瑩','脾','嘟','帕','噪','穫','縛','暈','裙','頸','竊','濁','峽','倘','蘊','餵','囊','霉','薇','剃','衍','訣','廂','臟','枕','慌','豔','湘','熄','琦','蓄','削','鵬','券','渺','臘','伺','蕾','矢','挨','漿','娶','廚','睜','虐','薛','蓬','垮','暨','鑼','遂','喧','釘','堵','醇','嬰','耕','濱','葬','履','艱','緯','姦','摯','鴉','蒸','葡','嚐','甫','璿','霍','尉','妓','棉','秉','爹','撈','綁','翩','嘸','呻','拂','貳','燭','懲','宴','撇','爍','汰','歇','癌','咕','崩','膩','撰','樸','棺','頌','魄','舜','蕃','寇','萄','妝','遼','襄','薯','曝','諮','蘿','頒','菌','嚮','氓','枚','酬','馮','嘲','橘','侮','灘','屢','歎','巢','髓','碑','梨','礦','疋','脹','賈','譴','悸','煉','胏','豹','擅','迦','蠶','肌','攀','卵','闢','炳','嘍','盞','鄙','浦','尬','弗','株','爪','抒','侍','阪','祇','逗','喉','栽','疫','黯','飼','鋁','鉛','劈','艘','仕','嶼','郊','釵','鵰','裸','嘯','璞','凶','頃','寓','狸','柄','挪','沛','鰱','咚','芷','彙','豎','僚','姜','窄','杖','倩','兜','廊','燙','惶','吶','祺','耿','鏘','綽','迄','柵','夷','拙','煥','妒','鷗','溯','蠅','沌','聆','潰','攪','吼','竭','磊','瞄','唾','棲','倡','掏','俺','浸','酌','繭','芙','楣','押','卦','苛','鴿','凸','匠','悼','蛛','繩','掠','暱','瞞','芋','蔥','墳','拯','啤','剋','逕','茵','佮','滔','崔','宛','贖','蟬','蕉','貶','裹','燄','朦','芽','御','狄','顫','倪','燥','啞','頡','樺','惰','荳','糧','貸','祐','炫','旬','噢','齣','鱉','簿','喘','綸','腥','敷','悍','袂','僵','尷','締','檳','紮','斧','襟','轄','肖','鈍','腫','檬','蹲','嗜','逾','瀑','罕','癒','碌','迋','稻','譚','撼','禎','裏','凋','哨','掘','澀','釁','汙','庚','慚','隧','膨','詐','釀','脂','圭','凳','鑫','槓','綺','拭','捏','拐','瑛','醋','蔚','筠','鶯','闇','伶','曬','鬍','膝','亟','卅','曠','抉','惘','溢','剖','喃','琉','竅','蝸','呃','匡','逮','榔','奕','傍','檸','鉤','襪','暇','扳','梵','泓','涅','刁','輾','蔔','斐','捍','聳','疤','蜘','姚','忿','恍','黛','瀚','諦','堤','窟','篠','仟','繡','暉','嗶','窺','晦','渝','禧','刃','沫','葵','匣','楠','隸','轎','嘔','蔽','綻','丞','諜','襯','晰','膏','窈','嚕','蘆','斂','皺','峻','孰','仄','瀏','涕','鈔','沮','擲','窕','煽','袱','蝕','絆','茹','瞪','丐','舅','詰','懺','鹹','錐','丑','淳','焚','溉','毓','蒐','戳','雛','闕','佰','鈺','哄','菱','肺','軀','芸','姨','壟','盯','奢','巾','槃','紗','菸','凹','腕','翟','怠','蟾','蔭','庄','寰','囡','瑄','饋','阱','靶','腎','擱','搏','闌','穆','呱','犀','飢','蹺','疵','瑤','樵','鴛','輒','閥','琨','憧','勻','搗','隙','悵','虞','跪','乞','逞','孽','瀰','榕','徽','蜀','螃','俏','淆','丰','萱','俯','敞','渣','緝','詛','紳','屐','眺','咫','溺','疆','饅','瓏','屯','沸','餃','鴦','夭','憬','駱','芹','葦','徘','竄','謗','啼','囚','絮','鐸','乍','蕙','杆','冗','簧','脊','眸','愿','趴','滯','貂','嘶','拱','掀','萃','彗','邵','徨','輿','朮','巍','徊','叩','妞','侏','苟','吠','嘩','憊','茅','矯','邂','檯','鎚','禽','棠','崖','澆','啄','挂','銜','朽','嫖','汐','揣','寥','徬','畜','瑕','氾','赦','筱','粥','稜','虔','湛','崙','瞻','懦','滲','儡','祿','簾','擒','萎','澈','蓓','磋','膳','瀉','蚤','椒','儕','塌','莽','琮','壤','矽','弧','茍','脖','憫','魎','鏈','蕊','鍛','奎','嚼','糗','楷','茁','偎','磅','笙','蔓','恃','隅','餌','裘','俐','拚','廓','鄒','烘','汀','鑄','崑','鑒','嚷','莖','噸','煤','勘','殲','樽','扔','杏','瀾','廈','噎','穢','馴','峙','厄','躬','僻','酥','毆','郤','曖','繽','伽','閔','蔑','茜','躁','誡','繕','咎','鏽','淌','曜','扛','頰','佫','麒','喀','蒞','芥','逅','雇','斟','菇','誦','瞳','苔','樁','懋','曳','滷','閏','耽','駭','糞','卯','岔','琵','蹋','禹','汲','倌','嗡','泌','捌','皂','晝','渦','岱','梳','莓','睿','鋸','瞌','轅','惕','廬','旻','遁','贓','礁','毯','絨','淇','甦','莒','粵','焊','瀨','隘','嫩','藐','垢','聶','譏','恤','怯','岫','巖','倖','訶','裔','蟄','吭','跤','嘰','梓','鎧','鱗','痘','朔','騁','驀','矇','椎','嚎','釐','橄','亥','龔','濛','俞','殃','幟','啃','欖','搓','瓣','妃','噱','埠','硫','裊','閻','狡','橙','蹄','薔','豚','炭','琶','冀','祟','喙','鷺','炊','糙','靡','塘','媳','筷','懈','嫂','廝','橡','瓢','暸','兌','攸','唆','塚','溼','搪','茄','膛','祉','氫','炬','挾','瓷','攬','苓','霆','贅','桐','鍍','狷','呸','嫉','踹','咆','砌','愣','蜢','藻','瘤','鞠','墅','瑣','呎','牟','睏','郡','鉅','饗','遐','胺','霄','猿','蝠','沐','摟','曦','錚','傀','煚','燼','韜','璇','艷','侃','疚','颺','蹦','恬','璧','霈','屜','篤','咽','荊','鵑','昶','諱','屌','憎','裳','陡','楞','洶','耘','嚨','莘','淼','嗤','酵','銓','煜','鷥','厝','轍','嗓','偕','揍','摺','簫','戌','烹','鞏','盔','傭','骯','烙','蚱','慷','嶸','徜','偈','焰','啾','誅','曙','藹','蚵','憨','峨','悽','磯','涓','蒲','茉','揉','閑','璟','饑','畸','鯉','鯽','銬','岐','雋','誨','稽','戊','臻','繃','扒','舵','巳','羔','睬','恁','癸','艙','紡','煒','韌','弔','娑','擷','冕','碘','豁','摳','肘','抨','曇','臆','熔','駒','壩','絞','疇','珈','肛','骷','朧','媛','嫣','榨','纜','褪','昀','趾','酹','柚','搔','羹','舖','眨','堇','靨','蝙','鞍','鏟','哺','惆','霓','癱','訕','蛻','沼','聾','憋','韶','枷','懊','惚','篩','巒','凜','丫','硝','忱','玖','嵩','拌','絢','褚','汎','葭','鸚','嶽','祁','矜','盎','噫','婊','筑','憩','鵡','羈','娥','鏢','硨','蒹','袒','塹','悴','瘡','俾','窘','亢','詬','扼','祠','厥','蜴','蛤','痊','茱','儼','笈','榴','騏','蒜','奄','髏','鬚','砰','迢','蜥','縷','鯨','葔','糢','吱','眩','棧','戮','夸','樟','杭','笠','咸','棘','慵','籬','庶','荼','捶','漣','櫥','吏','荐','芯','禾','巔','肋','侖','跆','恣','鳩','蔬','徉','跎','揀','艸','嚀','蜻','嬉','鱷','沁','嗽','瑾','藩','匕','鹼','酋','虜','噩','驛','奠','萌','嗆','墉','兢','躇','泠','梢','翱','儉','甸','薑','詣','翡','僥','竇','瘖','撓','蟀','蜓','躊','緬','憔','擻','梟','渲','耙','惋','塾','皈','訐','觴','眶','蛀','愴','殭','噗','灸','竺','幌','痲','稟','傌','欒','窯','羲','愕','塢','慟','炯','葷','澱','佼','腺','埸','膺','扑','繆','冶','綴','旱','灼','勛','沱','嘖','嗈','泄','耨','霎','儸','紊','噶','剔','孵','冉','圳','臼','抴','怔','侷','褒','蹉','粘','淤','雌','檻','彤','頤','俟','朕','綾','蠣','蕪','霏','梧','妾','殆','狙','諂','甭','煦','眛','扉','揪','瑚','酪','漓','瞇','諭','机','揖','蟋','匈','幢','瀕','雍','蠹','琇','閹','惦','渠','愷','嶄','兀','餒','餾','訢','嬋','炙','褻','迂','姥','鑿','玟','訟','漪','釷','葳','咐','骰','嫻','踅','猖','訛','辮','汶','咻','儷','佢','囝','烽','晏','葫','僱','踮','桔','誣','癥','囑','罣','飪','癖','彪','俘','咄','渚','褔','庇','侈','詔','縈','箔','舔','擂','璽','迺','鯊','鮑','疹','遑','藺','洒','桓','茗','辟','瞋','褐','熹','顱','弋','慄','蓊','羿','噬','籐','窒','碴','跋','肪','睦','罹','臀','槌','瘓','瀛','胚','揹','漾','卉','拇','釗','璀','娣','諺','鞘','吩','羚','鉗','晒','竣','熾','翎','惺','丕','洹','跛','勦','蛾','撩','翊','璁','氯','穀','譎','攘','痔','鈣','漱','噯','婿','瘀','軾','滸','漩','昕','垣','靄','尸','咯','剿','瞥','骸','咿','貍','磷','繹','槳','霾','棕','燿','筍','吽','遴','鎔','俑','咨','婪','敕','孺','訥','氮','矗','尪','寐','靴','裴','鵲','靚','仝','洸','磕','鬢','荻','隕','汞','蚣','佯','珀','瀝','咀','榷','暐','簇','鸝','隍','痺','鎳','椏','簣','籽','瘴','胥','徙','痠','濯','朴','撮','搧','弩','寅','殉','竑','堉','麓','嗔','蚓','睞','墟','疙','垠','蜈','嬴','崢','夙','嗅','仆','璜','峭','蜍','聿','蚯','闋','檀','鈑','罔','摹','鰻','蠱','葾','拈','媲','箋','湄','擄','鴕','謾','矚','垚','賬','躪','崚','樊','瘩','蔗','邃','亙','沂','韃','粱','蹂','旄','捫','諳','紓','叨','焜','螳','曄','劭','喈','漬','閨','瀆','乩','憚','雱','坷','奚','淮','拗','稠','睽','跩','酗','彆','浙','鋇','琢','誹','饕','齷','隼','箍','吮','陞','掐','蓁','寨','敖','驥','酉','咩','虱','酣','篷','癲','欸','媄','岑','湃','遏','驍','睭','万','匱','濺','簷','戾','滂','鑣','鬩','竽','芻','烜','銃','渥','燉','瞑','鑲','衿','粟','笆','摻','錘','吁','蛹','梖','恙','崛','烷','賏','孜','嶇','榻','綢','譙','遽','卍','爻','贔','葆','驂','娓','棗','餿','潢','庠','庵','剷','嚥','捅','垛','迭','圃','狽','嗦','町','鯰','漳','澹','隴','齪','厘','杵','蟆','哞','慫','姪','苯','揆','髦','懵','潞','詫','賂','琬','橢','佗','皎','詼','諄','峘','鏞','貽','壬','悚','摒','殤','邇','忡','逑','孚','劾','喳','糯','佣','濂','榆','緹','餡','馥','踝','鬨','迥','鎘','叱','拎','猥','悖','膿','鱈','柿','砥','潺','盥','臍','邰','腑','鎂','攢','隋','嗣','閘','碇','豺','冇','傜','梗','肄','萼','咁','搥','枋','沽','畝','衙','魷','鑾','篡','璨','錨','泯','拽','鎗','籟','蔫','戎','剌','貯','黝','徠','妍','沃','鈦','逵','唄','嗩','馭','恿','灶','昊','胤','鈿','闔','沬','琅','筐','浣','杞','牒','荃','鉦','艋','踼','驤','苞','痣','澗','洄','牯','啜','痰','莞','愜','嗖','煇','鮭','倏','藕','芮','麾','雉','鼐','仞','栩','菠','剽','狒','儺','柒','筏','妲','伎','睫','紜','輦','顰','哮','骼','螫','愫','裱','鐽','荀','晤','釧','雩','玠','吆','汨','糜','呷','毗','涌','弼','坍','垓','靦','乒','麴','黴','籮','噠','齁','悻','楨','鸞','悱','綏','旳','緋','歛','躄','偌','蒨','謔','冽','蜃','瞰','薏','腆','槭','宸','蝗','踱','餞','逄','浬','娼','劊','巿','屹','唧','唏','娉','潦','嗙','蚌','稔','乓','倔','哽','窠','烸','俸','淦','諫','譁','黌','碾','癟','鰭','檜','齦','毘','覷','帷','礪','魘','晌','缽','蜿','墩','浯','燊','捆','嵌','釆','謨','徛','脕','茸','獗','鯤','泱','栓','崧','啐','祀','崁','舫','陲','姍','捻','琛','蛟','磺','謐','咋','閤','瀅','蝌','鋤','埵','弛','箇','踞','窿','鼾','匝','荏','滌','踵','蹶','帑','糰','獃','燁','掬','吒','窪','燻','躋','弭','醞','傯','磐','夯','嗇','酯','捱','蕨','摃','葯','忝','嗟','絹','鉀','瞿','鰍','鄺','舶','晾','嬤','鞦','繾','萏','軋','嬸','狩','蚪','詒','爰','楔','擘','獰','縹','鷸','隹','埤','慍','猾','箝','餚','濡','蹬','騖','鐮','囈','芎','胱','湮','獺','嗝','恫','菡','琥','鈾','嚏','啻','邢','偃','楹','閡','颯','蟒','鼴','眈','謅','剁','宦','犁','翌','稷','閭','儐','忖','槐','箕','稼','箴','戕','喋','瘍','埕','甯','湍','暝','襠','綣','牴','叟','琍','懾','槙','薈','皿','沅','砷','逖','瑯','嫵','韆','佞','囤','篆','鯛','菈','梆','詆','軼','錮','饞','樕','猷','緞','頷','豨','迸','釜','蛆','愎','瑙','諍','瀧','鷲','阜','俎','褓','濘','玆','醃','攫','怦','昴','嵋','詡','宥','喫','暄','幗','甡','晞','跚','睪','臧','駑','纓','痧','璉','嘮','儻','捎','惻','睨','衲','杳','姣','拮','槁','彧','栱','婢','簑','忑','腮','鉻','蝨','躅','霽','忐','嬿','駟','炘','妤','忪','秧','渙','氨','滕','殯','躑','猙','戟','僮','馱','癩','鰣','聒','嫦','錡','謫','姒','餉','癈','驊','胭','菅','緲','淂','棣','姝','堐','据','紕','捺','犛','椿','嗷','嘈','醺','軔','涎','鹵','鈉','鏗','蜒','浚','婁','罈','嶙','蝟','郢','拴','蓀','鋰','邋','猝','倭','脯','滬','銲','甕','鱸','啵','悌','胳','胯','膊','爿','峋','涘','潁','獠','邑','腋','瘁','坻','暾','鮀','舴','岌','帘','柑','觔','桀','莠','喟','綵','袓','鈃','澍','耆','瞠','沚','珣','蛢','褉','糸','痢','腓','蹴','伝','勺','飴','熨','餛','芩','叼','韭','娩','誑','幡','鑠','膫','璐','鑞','嫡','犢','挓','唰','蕤','帛','庖','諉','晡','枰','淅','鋅','荔','紂','葩','緘','擰','躡','豊','烯','跺','甬','邸','氟','榛','璣','倜','焢','佚','疝','盅','噤','燴','窖','燬','珂','摀','櫓','佶','烊','淙','挹','菀','獼','卞','帚','洱','諛','鵠','鏤','洐','酮','蹛','炤','碉','蹣','坵','氦','蓑','藪','矬','臾','舀','蔻','儔','恚','菫','雎','匾','夤','熒','遢','哆','苳','踽','揩','棹','鳶','壅','謁','壑','鍰','謳','衹','渤','顎','沝','氰','蛭','呣','胛','涪','畦','颳','繚','邈','幄','睇','臊','刈','肓','臬','蹼','尻','捀','羡','泵','紲','孃','蠕','銂','轆','戍','刨','拄','渭','嘹','膾','蹙','啷','蠋','歿','絳','愍','礫','兀','夆','恪','淩','蝎','囪','嚶','蠔','贛','忉','捩','掣','撬','黔','罄','芊','矕','孑','伕','陛','脩','鎢','譟','揶','鄔','靳','陝','扈','痙','蔘','蹧','氐','趺','甥','蹊','躂','湠','謢','贀','亳','飩','賃','宕','苹','詘','嗄','粼','貲','榭','覦','纔','硐','圜','綑','嘀','鮫','岍','坳','葄','熏','刎','潸','鼬','顥','拺','昝','桎','頇','訖','婀','淬','輟','愔','揄','壼','趐','墬','稹','埂','蚜','靼','彊','沓','砉','罡','彫','諼','覬','褟','靛','鷓','屄','迵','欉','祚','銼','褸','攙','脛','筌','礡','珪','摑','柜','柰','崽','筊','蓼','蝣','賁','晟','椆','焙','雹','賑','賸','獷','昃','撂','鬟','炕','囿','軛','搾','簍','韁','婬','婓','瘐','鴝','囍','玷','幔','筵','糠','玎','堀','胝','倨','棻','鏖','掔','滮','熇','虌','仃','旌','袞','崴','鴣','翳','纂','畀','葚','鶩','俚','涔','涸','髻','颼','攣','宓','倬','綩','誏','軂','珞','愾','斡','耦','壕','濠','鍚','嗲','鰲','捂','腱','讒','忒','忻','萩','羌','寤','踫','錠','鐺','瓚','凊','紘','洵','盹','暘','錕','鎊','卬','芴','蕎','鴞','砝','胼','蛔','嗑','唅','栲','啖','甌','毐','埼','梏','琱','豋','擤','齰','迤','硯','篾','鐲','癬','驪','囥','玹','桹','詄','鋃','恒','弁','忸','啣','釦','瘠','鮪','偆','搵','漉','粿','儆','槤','祗','唳','戡','鉉','紈','皕','蜉','鴇','芍','掄','滇','皚','褊','駢','臏','黠','囁','鱔','湳','鍶','懟','閂','砧','痍','貉','慇','擢','璠','汕','听','啕','庾','輊','霑','謄','彝','斕','憭','懌','蕁','鎯','纇','衊','豕','腴','溥','蜷','褥','瞼','鬃','醮','鐳','焗','瞅','熠','嚓','黧','戇','奐','弒','氈','鮆','囓','惇','蜇','懍','撻','戽','渟','杷','舢','迨','冢','娌','斛','鄂','裨','燎','臃','餮','讖','秝','蕘','奲','佃','柢','軻','璩','扺','珗','焂','瑀','萹','踉','皖','鎰','襤','圴','侄','俵','凈','哧','頎','嶠','顢','灝','孓','岷','柬','鈷','輓','慼','瓔','种','惙','黽','瑮','闥','髯','橇','簸','咭','畬','綪','蹓','圻','冑','哂','曷','浹','覃','睥','釉','縞','汔','佘','媞','揕','榚','鄢','翦','鵒','莢','翕','萋','搆','鎬','蘑','騫','騾','荇','喢','寑','酢','殞','踰','醛','鱧','倣','陘','幀','鰓','欷','豝','酚','痾','皙','慳','碓','銖','暹','簌','攷','咈','肏','摽','醚','茨','舷','惴','鈐','綬','膈','豭','濬','旡','峈','洍','焯','殛','裾','撽','橞','嬲','泗','肱','匍','媾','蓆','鴆','澧','攆','玀','乜','偀','廌','嫭','坏','怵','晷','瘉','羸','柪','纍','硃','螻','昉','珩','茪','茯','淖','屣','慬','犘','蹌','淞','硼','犒','颶','蟠','覲','藷','亍','柎','柺','盻','衾','晢','喑','喏','噉','鋏','璗','鍘','碁','奘','畚','袈','諶','阯','岬','庛','荎','嗐','瑗','弈','絀','琿','粳','噥','磴','餽','驃','忤','舺','袪','碥','汾','怛','玥','兗','皋','皰','黍','蒿','賒','豌','檐','麋','砒','掂','跏','煢','艄','葑','壆','遶','錩','瞴','螯','鯁','瓃','蠑','苧','旎','孳','裟','錳','簪','霪','彳','扡','厎','柘','悀','砪','掇','嗒','媺','粲','懨','蹔','蹭','麤','杓','啁','鉑','頜','褶','醣','齟','鰥','掤','笳','脢','蛂','戭','蟘','妁','侑','倀','巽','漕','箸','殮','曩','魑','孥','殂','苠','党','凄','剮','豜','憍','囔','艮','幃','煖','冪','簞','瀲','齬','卌','惼','晹','裎','瑧','儰','撜','阡','姘','枸','栘','舨','瓠','脣','毽','濮','櫚','櫬','鼇','汜','岦','衪','郅','旂','茼','雃','犍','竫','摶','榖','儌','獒','闍','騄','糬','鬘','枇','陂','毬','廄','鞅','輜','褡','怙','琣','腊','痹','樨','濋','苒','掖','釭','媧','愆','楝','萵','銨','鴒','贗','洁','庳','馗','絣','傱','畹','潀','斲','貘','氖','狎','肴','痂','銑','褫','鍬','咂','坨','掞','摠','盦','鋹','鴟','顴','叵','篁','嬝','贍','峗','挴','窆','琚','竤','跫','撘','獪','鱒','伉','郃','涇','盍','鈸','旖','璘','瞟','縝','饜','扦','哖','悒','揃','稗','触','璊','閰','鍺','瞱','蹇','蹩','鵟','饌','佻','泅','盂','浥','赧','萸','睢','稞','潼','螟','夔','怜','邯','苻','雰','祼','艉','餬','燹','櫸','怏','枴','柞','洮','匐','堊','飭','瘧','燧','牘','霰','芃','妺','怢','怍','芫','苤','痒','螈','鍇','櫪','蚩','戢','賅','榫','薨','鍥','歟','魍','网','孢','喎','琡','嶂','噌','澔','諴','橿','襁','鞥','塋','痱','儈','瘸','蕈','櫛','璦','穠','鏜','矓','衢','卲','氡','迣','凎','揠','琰','綃','裐','鉞','鶻','矘','杠']



"""
for c in freq:
    filename = '/var/www/html/api/rfbackend/' + c + '.chardesc' 
    if os.path.exists(filename) == False:
        ask = "break down the character '"+c+"' into its components, give an example of use and make a one line story to remember it"
        ret = aisocketapi.ask_ai(ask)
        fp = open(filename,'w',encoding='UTF-8')
        fp.write(ret)
        fp.close()
"""


count = 0
for c in freq:
    filename = '/var/www/html/api/rfbackend/' + c + '.chardesc' 
    if os.path.exists(filename) == True:
        fp = open(filename,"r",encoding='UTF-8')
        text = fp.read()
        api.process_chinese(''+c,"ai",text,constants.CWS_TYPE_DETAILED_CHAR_INFO,-1)
        count+= 1
        if (count > 2000):
            exit(-1)
"""
    if database.find_word(c) == None:
        dd = dd + ' ' + c
        if (len (dd) > 500):
            api.process_chinese('imported char','process',dd, constants.CWS_TYPE_IMPORT_TEXT,-1)
            dd = ''
"""