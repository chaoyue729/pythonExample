import random

class CallText:
    stt = []
    stt.append('안녕하세요 올레 모바일 음성 사서함 입니다\n음성요금은 일반 연락번호를 남기시려면 이번을 눌러주세요\n음성로밍 일반\n연락번호를 남기시려면 이번을 눌러주세요 음성요금은 일번 연락번호를 남기시려면 이번을 눌러주세요\n확인하고 다시 이용해 주세요 이용해주셔서 감사합니다')
    stt.append('여보세요 아 네 안녕하세요 고객님 여기 케이티 전화국입니다 네 아 예 고객님 아닙니다 고객님 요신 죄송하고요 고객님 였습니다 꽂아 선자 휘자\n그 카드번호요 네네 아 아들이에요 아들 아 아드님이세요\n네 아 예 그 우선은 제가 전달받기로는 봐드릴게 해지 하기로 하셨는데 예예 해지가 안됐다고 하셔가지고 예 연락을 드렸\n제가 요거는 아니 해지도 안 됐잖아요 지금 확인을 좀 해보고 연락을 드린거예요 고객님 확인한건데 없으세요 예 그래서 이거는 저희 직원때문에 이렇게 불편함드려서 였습니다\n기기가 너무 죄송 아 그럼 내가 해지상 해지한 상태는 맞는데 그쪽에서 잘못한 거에요\n아 지금 그걸 요즘은 왜냐면은 해지를 하실때 이제 신분증을 이제 저희쪽에 넣어주시면 제가 팩스 넣어 떨어져 다 했던걸로 알고있는데요 어차피 녹취하잖아요 네 그렇죠 화명동 예 그럼 신분증은 그래서 이제 보내주신 부분은 맞는데 여쭤보는 거에요 고객님\n예 아 예예 그 우리 어머님 휴대폰 있는데 오늘 발송 한번 이거 가지고 예예 내가 뭐야 저거 까지 해가지고 다 아 다 알려드려봐도 직접 보내면 되고 아 너무 죄송합니다 그럼 이걸 제가 어디 죄송하다 그럼 어떻게요\n아 예 그럼 지금 여기 그럼 계속 나가고 있었던 건가요 예 그런데 그거를 이제 고객님께 저희가 돌려드릴 위해서 좀 안내를 해드릴려고 연락을 드렸습니다 고객님\n예 아유 너무 죄송하고요 그럴때 유월달에 연락주셨더라고요 고객님 네 그 오월달 요금이 유월에 나오시고 이제 유월달 요금이 합산으로 이렇게 후불제 나올 순\n네 우선은 그 유월달 이용요금이 칠월 나올수 있는데 네 그 칠월 청구서부터 사용하시고 칠 팔 구 시월달까지 요금이 다섯 달치가 납부가 되었더라고요 고객님 아이피 사개월 시월달\n그니까 까지고 가게쪽은 지난달에도 지금 어머니 번혼데 어저께 말이 됐잖아요 지난달에도 빠져나갔다는 이미 십 일월달에 는요 고객님 지금 통장 예금이 없으셔가지고 우체통이 안되셨습니까\n그래요 예 그거는 그럼 저희가 지금 출금이 안된 아니 제가 영업점 지금 해지를 하세요 예 해지가 된 상태에서 이제 아니 지금 제가 이제 제가 해지를 하고\n그 다음에 그 일단 내신 요금을 제가 고객님께 저희가 환급을 해드리면서 그 다음에 예 지금 이제 해지가 되시면은 이제 그 이월달까지 요금이 나오시는데 그 부분까지도 저희가 다 면제 처리를 제가 알 수납을 해드릴 거거든요 고객님\n그래서 저희가 저기 요금을 환급을 드릴려면\n예 저희가 이제 그 명의자님 본인 명의로 된 통장으로 저희가 환급을 해드립니다 어머니랑 통화하세요 아 예 전화번호 알려주세요 어 아 이거는 지금 여기 자동이체 그 농협 통장이 그 박 선자 휘자 님 명의로 된 틀렸더라고요 일단 저희 어머니랑 통화를 지정하신 아 그렇게 하시면 될까요 고객님\n아 예예 예 그러면\n연락처는 어떻게 되실까요 고객님 공일공 예예 이 육 오 오 이 육 오 오 육 팔 칠 이요 팔 육 칠 번이시고요 고객님 네 근데 그냥 그 그 뭐야 그거만 완납해 주고 그쪽에서 뭐 뭐 뭐 상품권이라도 한 안죠\n죄송합니다만 이 그런거\n그래서 잠깐요 예 왜냐면 저희가 이제 그 부분으로 해서 칠 아니 어쨌든 취소를 본 부분인데 그것도 이제 실제 손해본 부분은 저희가 바코드가 다 돌려드리는 부분이고 그리고 알았어요 예 너무 죄송합니다 어머님께서 그럼 그쪽으로 그 환급 해가지고 진행하도록 하겠습니다 고객님\n예 예 너무 죄송합니다 예')
    stt.append('고객과 소통하는 와이브로 상담사 이 규대 입니다 무엇을 도와드릴까요\n아 지금 와이브로 에그랑 넷북을 쓰고 있는데 예예 고객님 이거 두개 혹시 정지 가능한지 확인해주세요 아 그러세요 제가 바로 확인해보겠습니다 우리 와이브로 명의자분의 생년월일을 말씀\n시겠습니까\n팔십 팔년 구월 십 이일 이요 명의자분 성함 말씀해주시겠습니까 오 상희 조 성희 님 이시고 상희 요 고 상 님이시고요 네 여성분이시고 전화주신분이 우리 명의자분 본인이신가요 네\n우리 고객님의 청구지 주소가 어느구 어느동인지 확인 부탁드립니다\n청구지 지금\n천안시 서북구 두정동 돼있나요 어 아닙니다 다른 지역으로 되어 제주시 연동 예 소중한 정보 확인 감사드립니다 네 현재 와이브로 에그 확인되고 있고요 네 예 약정은 이미 다 끝난걸로 확인되고 있습니다 네\n네 고객님 이거 제가 해지할려 그러는데 당장 시간이 없어서 어떻게 해야되나요 해지하시는 방법은 두가지가 있는데요\n전화는 케이티 플라자라고 해서 예전 전화국으로 신분증 가지고 내방을 하시거나 아니면 팩스나 프린트가 가능하면 저희 고객센터 통해서도 해지 접수는 가능한데요\n네 확인 할까 미납이 있기 때문에 미납요금 다 납부하신 다음에 해지 접수가 가능합니다 아 미납이 있어요 네 그렇습니다 어 얼마 있어요 예 지금 미납요금 제가 확인해보겠습니다\n지금 아 예 두달이 미납이 됐네요 총 이만 천 팔백 육십 원 확인되고 있습니다\n그 이거를 돼야만 해지가 가능하다고요 네 맞습니다 그럼 정지는 가능한가요 일단 지금 저희가 일시정지는 가능한데요 네 일시정지 좀 해 드릴까요\n얼마나 이십 원인거에요 일년에 횟수로는 네번 일수로는 백 팔십 일 정지가 가능한데요 예전 일시정지 기간에는 기본료는 청구되지 않지만\n그래서 유지 비용이라고 해서 한달에 부가세 포함해서 삼천 삼백 원이 청구가 됩니다 네 네 그렇게 해주세요 네 정지 바로 처리해드릴게요 네 정지는 일년을 했었는데 번 일수로는 총 백 팔십 일 정지 가능하고요\n네 기간 동안에는 한달에 기준으로 부가세 포함해서 삼천 삼백 원이\n기본료 제공 데이터 날짜 계산돼서 청구가 되고요 네 복구할때는 명의자분 본인께서만 미납 요금 없는 상태에서 복구가 가능한데요 혹시라도 백팔십일이 지났는데 정지를 복구하지 않으면 이용중단 상태로 변경이 되었다가\n또 추가로 삼개월이 지났는데도 복구하지 않으면 직권해지라고 해서 자동해지돼서 등록 될수 있고요 요청하셨던 일시정지 바로 완료 되었습니다 네 그 데이터 속도 있는데 그게 지금 제가 해지를 했는지 기억이 안나서 것도 한번 확인\n와이브로 고객님은 지금 와이브로 하나만 확인되고 있습니다 예 그러면 아 그거 하나밖에 없어요 네 아 네 알겠습니다 네 감사합니다 네 와이브로 상담사 이 규대 였습니다 네')
    stt.append('행복을 드리는 케이티 서 유리 입니다 여보세요 네 고객님 인터넷 이거 이전 좀 할려고 그러는데요 아 그러세요 명의자분 생년월일과 성함 성별 말씀해주시겠습니까\n팔 공 하나 하나 둘 둘 이거 남지 하고요\n한 정수 요 네 제가 잘 못들었는데 팔 공 하나 하나 둘 둘 맞습니까 예예 한 종숙 고객님 맞습니까 영신이요 정 수정 한 정수 고객님 이세요\n예예 잠시만 기다려 주시겠습니까')
    stt.append('행복을 드리는 케이티 정 다영 입니다\n여보세요 네 고객님\n네 아 제가 그 인터넷 지금 요금 확인을 좀 하고 싶은데요 아 그러세요 근데 고객님 혹시 집에 설치하는 그런 인터넷을 말씀을 해 주시는 거세요 아 네 그니까 제가 그 결합\n요금을 좀 확인했다가 인터넷에서 만원 할인을 받고 있는데 뭐 때문에 할인받고 있는지 좀 궁금해서요 기억이 안나서 아 그러세요 제가 따로 핸드폰 담당부서이기 때문에 인터넷 할인 받는 내용까지는 확인이 안되세요 아 그렇죠 그러면은 네\n즉시\n아 그 그냥 이용 지금 이용중에 네 그 이십프로 할인받는거 있잖아요 약정인거라서 할인 받는거죠 네 그거는 요금제 상관없이 신청하면은 바로 받는 건가요 요금제도 가입 가능한 요금제가 있고 가입안�는 네\n저희가 있으세요 문의하시는 번호가 공일공 구 일 사 구 사 오 이 칠 번호 박 범준 고객님 명의자분 본인이세요 네 네 우리 고객님 예 네네 말씀해주세요\n순 요금제로 해도 그게 해당이 되는건가요 순액 요금제는 할인 받아볼수있어요 아 그 순 순 삼 사 요금젠가\n네 그런 거 그 선 들어간 요금제는 다 할인이 적용되는 거에요 순 모두다 올레 삼 사 요금제는 따로 약정기간에 따른 요금할인 이십프로 할인받아보\n이요 아 그 궁금한게 만약에 그 약정을 걸면은 네 제가 지금 쓰리지로 쓰고 있는데요 네 그니까\n이걸 나중에 엘티이로 요금제를 바꾼다 하면했다고 그 약정은 상관없는 거죠 그 안에서 요금제 바꾸는 거는 아니요 안 되세요 그 약정이 쓰리지 약정이 있고\n네 해지 약정이 있으세요 네 일단 요금제에 따라서 일단 할인이 들어가시거든요\n네 만약에 고객님께서 지금 단말기는 엘티이 고 어 요금제가 쓰리지라고 하면은 제가 고객님 스마트 스폰서로 가입을 해드리잖아요 우리 고객님께서 추후에 쓰리지 요금제로 나 뭐 엘티이 요금제로 자체가 변경이 안되시죠 왜냐면은\n쓰리지같은 경우 쓰리지 단말기에 유심을 장착을 해야지만 쓰리지 요금제로 변경이 가능하고 엘티이 요금제는 엘티이 단말기 엘티이 유심칩만 이렇게 가능한거잖아요\n그러면 추후에 번호 그 유심이동을 하셔야 되는데 요금할인 이십프로가 유심이동 자체가 안되세요\n아 그래요 네 육십 는 제가 지금 아이폰파이브를 쓰고 있는데요 네 이게 둘다 됐는데 저는 쓰리쥐로 쓰고 있다가 제가 올레 직영점 가서 유심은 엘티이로 바꿨어요 네\n근데 쓰리지 일단 유심 바꾸고 이제 요금제 제가 엘티이로 바꾸면 바로 변경이 되는데 이런 경우에도 같은 해당이 되나요 아니요 지금 엘티이 단말기 엘티이 유심칩이라는 말씀이시잖아요 그러면은 네 주세요 그럼 엘티이 스폰서로 들어가면 되는 겁\n아 그러면은 약정을 걸 때 아주 복잡한거 같네요\n아\n네 유심이 갈아끼 이제 유심이 그대로 할인이 적용된다 이말씀이죠 아니요 상관없이 문제가 아니고요 휴대폰 쓰리지 요금제로 변경을 할려고 하면 쓰리지 단말기여야지만 처리\n주소로 변경이 가능하고 엘티이 요금제같은 경우에 엘티이 단말기 엘티이 유심칩만 엘티이 요금제로 사용이 가능하세요 아 그 경우에는 저희가 되거든요 지금 등록되어 있는 주소 동까지만 일단 말씀해주시겠어요\n아 서울시 관악구 남현동 확인 너무 감사드립니다 지금 단말기는 엘티이에 유심칩도 엘티이 맞으신데요\n네 그러면 쓰리지 요금제 사용중이시잖아요 네 만약에 고객님께서 엘티이 요금제로 변경을 하면은 변동이 되시는데 네 나서 고객님께서 이제 쓰리지 요금제로는 변경이 안 되세요\n아 한번 하면요 네 왜냐면은 아파트 쓰리지 단말기로 장착을 해서 유심이동 자체가 안되는거잖아요 내방하는 일반기변처리하시고나서 요금제도 바꿔주셔야 되기 때문에요\n아 그래요 그러면 유심칩만 바꿔서 끄는게 안되고 요금 하루\n아 그러면은 엘티이로 요금제 변경하고 약정도 바로 할 수가 있는 거죠 네 왜냐면은 지금 같은 경우 요금제가 쓰리지 요금제기 때문에 만약 가입하신다고 하면 제가 엘지 그 스마트 스폰서 쓰리로\n제가 적용을 해 드려야 되는데 내용은 추후에 고객님께서 요금제가 변경이 안되는거잖아요 단말기 쪽에 에다가 네 네 엘티이이기 때문에요 유심 자체도 안되실까요\n아\n저 아 저 혹시 결합하면 결합할인은 다른 분한테 물어봐야 되나요 상담사분 네 인터넷 할인은 유선쪽으로 문의하 해주셔야 되는데요 한번 상담받아볼 수 있도록 제가 연결을 해드려도 괜찮을까요\n아 네네 네 그럼 추가적으로 더 문의하실 내용은 없으시고요 네 네 지금 바로 연결 처리 해드리도록하겠고 인터넷에서 할인 받는 부분때문에 그러신거 맞으시죠 아 그게 그 쓰리지 인터넷하고 결합할인을 하고 있는데\n결합은 되어 있으세요\n아 네 근데 요금제가 엘티이로 바꾸면 은 할인된 요금이 달라진다고 하시더라고요 그래서 얼마가 할인이 어떻게 변동 되는지를 물어보고 싶어서요 그거는 저희쪽에서 상담이 가능한데 현재로써는 팔천 원 받고 계세요\n네 순 모두다 올레 삼 사 요금제로 변경을 하실 생각인거잖아요 아 엘티이를 전화 하면은 엘티이로 바꾸면은 할인이 어떻게 돼요 그게 요금제에 따라 틀리세요\n아 그럼 삼사로 기준 하신다면 그러면은 엘티이 순 모두다 올레 삼 사 요금제로 변경하면은 엘티이 뭉치면 올레 원으로 들어가거든요 그러면은 이천 오백 원 할인 들어가세요\n아 가천리 이천 원으로 다운되는 거에요 네 이게 요금제에 따라 또 할인이 들어가시는 거기 때문에요\n아 그럼 인터넷쪽에 할인요금은 동일한거고요 인터넷으로요 할인율은 저희쪽에서는 확인은 안되고 요 그거 네 그쪽으로 한번 상담받아 볼수 있도록 연결해드릴\n아 네 알겠습니다 문의 하실 내용 없으시고요 네 우리 고객님 편안한 상담 이어가세요 저는 케이티 정 다영 이었습니다')
    stt.append('행복을 드리는 케이티 강 효림 입니다 요금제좀 변경할려고 하는데요 아 그러세요 문의하시는 번호가 공일공 사 공 일 일 에 공 삼 오 일 번 이용하는 게 맞습니까\n니까 네 명의자분의 성함과 생년월일 말씀해주시겠습니까 네 순 영민 이요\n네 생년월일 구십 년 일월 오일이요 아 네 확인 감사합니다 제가 지금 조회해보고 도움드릴텐데요 고객님 명의자분 본인 맞으신 겁니까 네\n조회중에 있는데요 예\n지금 현재 우리 고객님께서 지금 이 번호에 지금 등록돼 있는 주소 경기도 성남시 수정구 다음 주소부터 말씀해주시겠습니까\n네 신협 이동 칠백 이십 번지 네 확인 감사합니다 변경을 하고자 생각해두신 요금 상품이 있습니까 그 삼사요금제\n순 모두다 올레 삼 사 말씀한 거세요 예 그 지금보다 한단계 낮추 있는건가요 고객님\n순 모두다 올레 삼 사 가 아니라 만약에 현장에서 낮은걸로 하면 순 요금제 기준으로 순액 모두다 순 모두다 올레 이 팔 요금제가 있습니다 따로 고객님 정확히 저녁에도 신거는 없는 거세요\n어 그 제가 요전에 그\n예 바뀐건지 어떻게 된건지 모르겠고 지금 이전 사용했던 요금제가 엘티이 삼 사 공 이긴 했는데 이 요 네 관계가요 그 요금제 지금 현재 가입이 제한된 요금제가 맞습니다 아 그래요 네\n일정만 생각해보고 아 그러세요 네 알겠습니다 추가 궁금한 사항 있습니까 아니요 네 우리 고객님 요금제 생각해보고 문의주시면 도움드리겠고요\n고객님 다음에도 연락주시면 되겠습니다')
    stt.append('행복을 드리는 케이티 한 강춘 입니다\n네 수고하십니다 감사합니다 어떤 내용이신거세요 그 제가 그 가입해 놓은 그 홈폰이 있거든요 네\n이게 그 제가 알기로는 십 일월달로 끝난줄 알았는데 네\n자녀분 물어보니까 뭐 더 있어야 된다 그래서 아 제가 그 케이티 그 영업소\n기사를 방문했거든요 네 그리 그리 갔더니 위약금없이 해약할수 있다고 뭐 아버라는데 걔가 지금 가기도 전화를 일단 먼저\n아니 드릴라 그러거든요 아 그러세요 고객님 네 죄송합니다만 해지 상담은 저희쪽에선 좀 어려우신 부분이라서요 네 해지 부서 담당자분이 다시 연락을 좀 드려도 괜찮으시겠어요 네네 네네네\n통화가능하신 휴대폰 번호 몇 번이세요\n공일공 네 팔 구 삼 칠 네 이 공 공 이 번이요 네 저희쪽에 고객님 인증을 해주셔서 가입자분이 윤하 고객님의 정보 확인되고 있습니다 사용하시는 번호 저희쪽에 창전동 에\n있으신데 맞습니다 담당부서쪽에서요 두시간 이내에 연락드릴 수 있게끔 내용 전달드리도록 하고요 네 방문하셨던 지점은 어디세요 전주소\n부천지사로요 이천 아 죄송합니다 고객님 이천 지사로 내방하셨던 거에요 네네네 네 알겠습니다 확인하고 전화드릴수 있게끔 전달드렸고요 추가 다른 더 문의사항은 없습니까 네 감사합니다 즐거운 하루되세요 상담사 함 강춘 입니다')
    stt.append('행복을 드리는 케이티 신 유진 입니다 예 저 다른게 아니고요 전화요금이 미납됐다고 문자와서 전화드렸거든요 아 그러세요 전화번호 말씀해주시겠습니까 공 사 삼 네\n이 삼 팔 에 이 일 일 구 요\n네 해주신 박 정자 란자님 본인 되십니까 예예 네 요금이 총 이만 삼천 칠백 이십 원 미납있습니다 그러면 혹시 지금 농협 통장에서 바로 출금 가능한가요 아 고객님 그러세요\n예예 아 네네 근데 잔고 지금 자동이체 되어 있는게 농협인데 예 이거가 있으면 십 이월 칠일날 지금 출금 예정이거든요\n아 근데 이게 옛날 까지 내일까지 안내면 저 전화가 끊겼다고 문자가 왔어요 그러면 십 이월 칠일 아까전에는 잔고를 비워놓으셔야 이중납이 안되시는데 괜찮으세요\n아 예 그러면 계좌번호 말씀해주시겠습니까 삼 공 일 네 공 일 삼 공 네 삼 오 팔 육 네 일 일 이요\n네 이만 삼천 칠백 이십 원 바로 결제 하겠습니다 네 다른 문의사항 없습니까 네 어 가득한 하루 되십시오 네 유진')
    stt.append('행복을 드리는 케이티 김 완태 입니다 네 지금 저희 와이파이가 네\n전혀 작동을 안해서 인터넷을 사용을 할 수가 없거든요 아 그러세요 불편드려 죄송합니다 고객님 제가 먼저 사용하시는 회선 조회 좀 해 드릴텐데요 네 연락주신 번호로 조회한번 해봐도 되겠습니까\n감사합니다 혹시 실례지만 사용하시는 지역이 어느 동이세요 여기 금곡동 이요 네 금곡동 몇번지입니까 백팔십오다시 이십 이요 네 계약자분 성함도 한번 말씀해주시겠습니까 김 은자요\n확인해주셔서 감사합니다 회선 조회는 한번 더 되었고요 네네 지금 확인해보니까 어 실례지만 저희 케이티에서 와이파이 장비는 따로 제공되신 건 안 보이시는데요\n혹시 광현 이요 네 다시 마지막 말씀이실까요 네 그 와이파이 장비가\n혹시 저희 케이티 장치는 확인 되시는지 남 인데요 네 그러면은 혹시 공유기 연결해놓으신 건가요\n어 이 와이파이 중에서 이게 케이티건데 아 그러세요 고객님 어떻게 되셨어요 고객님 미리 모양이 어떻게 설명해야 되나요 어\n예\n했는데 그냥 중동쪽으로 약간 남겨져있는 거니까는요 고객님 검정색이요 검정색이고요 네 실례지만 그 장치 에요 네 뭐 그 찍혀있는거 혹시 있으세요\n그러면 올레마크 랑 뒷 부분이오\n저희가 보통 그 모뎀 이실 가능성이 있으시거든요 고객님\n옛날에 인터넷 전화하고 싶어 갖고 거기서 같이 설치해 준거거든요 아 그러세요 고객님 실레지만 모양이에요 혹시 이렇게 둥그렇게 기왓장처럼 생긴 모양이 상태인가요\n네 기가짜리 그 기왓장이라고 했는데 그 약간 나온게 까 그 기왓장이요 지금 원래 그냥 전체적으로는 상탠데 네 이렇게 엎어놓으면은 이렇게 좀 약간 타원형으로 이렇게 둥그렇게 된게 현장 씨 맞나요 고객님\n번호를 타운 고객님 불 들어오는 부분이 어떤 어떤 분이 있으세요\n지금 전원버튼이랑 인터넷 무선 네 팔기가 지금 불 들어오고요 그 밑에는요 고객님 이게 통화중이라 업그레이드 그쪽은 안되는 거세요 아 그러세요 고객님 그러면은요\n지금 그 상태가 저희 케이티가 와이파이 장비가 맞고요 네 그러면은 그 실례지만 선 이렇게 직접 꽂아서 쓰시는 컴퓨터 인터넷은 되세요\n아니요 무선인터넷을 했어요 다 무선은 네네 아 그러세요 고객님 그럼 일단 제가 전산으로 신호상태를 한번 진단을 해봤는데\n예 지금 전산으로 진단해본 결과 댁내까지 신호 확인 필요한 상태로 진단이 되고 있습니다 네 그래서 통화 끝나면 제가 먼저 창치 초기화를 한번 해드릴건데요\n고객님께서는 인터넷 연결된 모든 장치를 저랑 통화 종료후에 꺼주셨다가요 다시 한번 켜셔가지고 와이파이 연결이 되는지 확인을 한번 해봐주시고요\n네네 네 저희가 이렇게 초기화 해드린다음에 유 연결 와이파이 연결 정상적으로 잘 되는지\n네 저희 케어 상담사가 넉넉잡아 삼십 분 안으로 고객님께 연락을 한번 드리겠습니다 네네 연락받으실 핸드폰 번호 말씀해주시겠습니까 똑같이 해주시면 제가 지금 전화번호랑 아 죄송하게도 불러주시겠어요\n공일공 육 삼 하나 구 사 삼 사 공 이요 공일공 육 삼 하나 구 일 사 삼 사 영 맞습니까\n네 알겠습니다 지금 초기화 먼저 해드렸고요 네네 남겨 주신 이 핸드폰으로 연락드릴 수 있게 신청도 해놓겠습니다 네 알겠습니다 네 항상 건강하세요 네 케이티 김 완석 입니다\n네')
    stt.append('여보세요 예 고객님 여기 케이티 카드 고객센터 이 선영 이고요 혹시 메일 들어온거 확인되셨어요\n거기 저기 메일이 지금 잘 안 떠서 확인하지 못했어요 내일 을 확인을 하시면 거기에 입력하라고 창이 하나 뜨셨을거에요 그 숫자를 입력하고 들어가셔야 메일을 열어서 보실수가 있는데 혹시 메모 가능하세요\n시만요\n여보세요 여분의 병무청 아이디고요 네 문자가 하나 삼 구 사\n일 삼 구 사 요 네 공 칠 구 공\n공 칠 공 하나 이 삼 칠 공\n하나 이 삼 칠 공 네 요거 입력하셔야 메일로 열어서 보실 수 있으시거든요 칠 삼 구 사 공 칠 구 공 일 삼 칠 공\n하나 삼 구 사 공 칠 구 공 이 하나 이 삼 칠 공 맞습니까\n공 하나 이 삼\n일 삼 구 사 공 칠 구 공\n일 이 삼 칠 공 네 공 하나 이 삼 칠 공 이요 이렇게해서 입력하시면 고객님 정상적으로 열어서 보실수 있으세요 네 지금\n그 병무청 아이디 면 지금 저희 에껄로 들어가서 보내 소리죠 네 당연하죠 고객님 명의자가 자녀분꺼 잖아요 메일만 고객님한테 임시로 지금 받으신 것 뿐이지 로그인 하실 때 이분의 정보 넣어서 들어가셔서 보실 수가 있는 거세요\n근데 아까 제 메일로 뛰어갔더니 그냥 그 생년월일 여섯자리 앞 여섯자리 미라고 돼 있던데 생년월일 어떤거를 말씀을 하시는거죠\n예 저 자기 본인 그거면 을 해줘요\n생년월일 앞자리 넣어서 지금 안열리신거 아니세요 예 그니까 고객님 거기에 문구가 그렇게 적혀져 있을지 모르겠지만 이 분을 생년월일로 저희쪽에 접수하신 분이 아니시거든요 병무청 아이디로 접수 하신거라서 병무청 아이디 넣으셔야 되세요\n아 그 일 삼 구 사 공 칠 구 공 일 이 삼 칠 공 이라고요 네 네 알겠습니다 감사합니다 네')
    stt.append('여보세요 네 안녕하십니까 케이티 였습니다 예 네 고객님 확인해보니까 시내전화는 정액 요금제 맞춰서 있지 않고요 시외요금만 시외 정액 요금제 가입되어 있으세요\n아 우리 그러면 데도 다 전화기가 됐는데 왜 해지 됐습니까 예 없습니다 고객님께서 해지하신 부분은 아니신가요 아 그렇겐 안 되시죠 예예\n해지하신 날짜를 제가 확인을 해보면요 예 확인해보겠습니다 잠시만 기다려주세요 우리 저희쪽 했을땐 얼마 일주일 됐습니까\n예전에는 만 오백 원이었어요 고객님 네 그래서 고객님 지금 시외전화 자동으로 사용량이 많이 없으셔서 폐지가 되었는데요 지금 만 오백 원이었어요 시내전화가 그래서 지금 고객님 만 오백 원 이상\n황 요금을 사용하시기 시내전화를 만 오백 원 이상 사용을 하시면은 만 오백 원만 청구가 되고요 예 만 오백 원 이하로 사용하시면은 사용하신 요금만 청구가 돼요 네 그렇기때문에 시내전화는 해 지금\n자동 해지가 되었는데요 고객님께는 이 이에요 아 그러세요 예예 네네 그러면 우리가 있잖아요 언제 세대가 되는 거 이거 날짜 나올수도 있으니까 시내전화 지금 자동으로 저희쪽에서 해지처리가 사용량이 많지 않기 때문에 고객님 편의를 위해서 해지전\n어떤 부분이고요 이거는 지금 확인을 해 보면은 시외전화 지금 만료 있습니다 이천 십 일년 대송 합니다 지금 이천 십 일년 시월 이일자로 장기 우대 로 저희가 자동 해지가 되었어요\n네 고객님 그러면 티비는 이전에 그러면 우리가 정해주셔야 됐을때는 전화요금이 한달에 얼마 나는거 좀 봐주실래요 언제쯤 요금 맞습니까 해지되기 전에 야 그 전에는 최저 시내전화요금 정액제 해지되기 전에 야\n네네 그 그 전화요금 지로에는 요금이 얼마 납부 죄송합니다 지금 그때 당시에 요금은 저희쪽에서 조회가 안돼요 고객님 이천 십 일년도에 예 고객님 해지가 됐어요 만 오백 원씩 요금을 낼 개통하시다가요 예 이체 근데 십 이천 십 일년\n년 시월 십 삼일자로 시내전화 같은 정액제는 해지가 되면서 네 그니까 만 오백 원 이하로 사용하시면 사용하는 요금만 청구가 되고요 아 만 오백 원 이상 사용하시면 만 오백 원 요금만 청구가 돼요 긍까 고객님께서 좋으세요\n살펴보면은 네 지금 올해 유월달에도 요금을 보면은 시내전화 실제로 사용한 요금은 만 이천 오십 원인데요 네 지금 네 만원 만 오백 원 이상 사용을 하셨잖아요 예 그렇기 때문에 만 오백 원이 청구가 되셨고요 당월에 요금을 보면은\n시내전화요금을 보면은 있습니다 음 오백 원 이하로 사용하셔서 사용하시면 육천 삼백 구십 원만 청구가 되는 거에요 아 만약에 제가 일단 넘었다 그러면 그거만 그거까지 만 오백 원입니까 네네 네 그리고 만 오백 원 이하로 실제 사용\n사용량이 그렇게 하면 할때 사용한 요금만 청구가 되고요\n아 예 그렇습니까 네 알겠습니다 네 더 궁금한 점은 없습니까 없습니다 예 행복한 하루 되세요 배 예 정원 이었습니다 네')
    stt.append('국민의\n사 팔\n니다 예 뭐 하나 여쭤볼려고요 드릴까요 여보세요 네 네 십 일월 삼일날 핸드폰 이제 개통을 했는데 네 고객님 네 카드를 하나 만들어가지고 네 카드사에 삼십 매월 삼십 만 원\n스마트 게되면 보조금으로 이제 국민카드로 했더니 구천 원씩 지원해준다 그랬거든요\n네 고객님 예 그 청구서를 네 이 국민 카드번호로 저기 저 저기 결제를 할려 그러거든요 아 그럼 자동이체를 신용카드 국민카드로 핸드폰에 등록을 해드릴게요 예 입증하시는 거는\n공 구 사 영 삼 에 삼 사 칠 영 번 맞습니까 예예 맞습니다 명의자분 성함 안 국영\n맞습니까 예예 맞습니다 한가지만 더 여쭙겠습니다 예예 네 주소지가 아 현재 경기도 구리시 다음 주소지 말씀해\n일단 이동 동문일차 백 이동 사백 이호요 확인 감사드리고요 고객님 카드번호 말씀해 주시면 바로 변경 하겠습니다 예 구 사 사 오 네\n사 이 공 구 네 팔 공 일 구 네 오 공 팔 칠 혹시 유효기간도 확인 가능하십니까 고객님 유효기간은 뭐 칠백 이십 인제 뭐에요 시월 십\n네 하고 쓸라고 인가 뭔가 해가지고 있어요 아 그러세요 이천 이십 년 시월달 이라는 거고요 아 인터넷 해지 싸다고 확인 할게요 구 사 사 오 네네 사 이 공 구 팔 공 이 구 오 공 팔 칠\n네 확인해보니까 이미 고객님 현재 불러주신 카드로 자동이체 등록이 되어있었습니다 그럼 혹시 네 혹시 우리 집사람 것도 한번 확인할 수 있나요 같이 했는데 같이 개통했는데 제 카드를 갖고 내가 또 어요 핸드폰 번호 맞\n까 공일공 네 칠 일 구 칠 하나 하나 구 삼 사 칠 요 칠 하나 하나 구 맞습니까 예예 그래 이거 삼 사 칠 이요 명의자분 성함 생년월일하고\n니다 손님들이 아니고요 네 육 공 공 칠 일 이요 네 주소지도 앞에 말고 똑같애요 동일하십니까 예 예 먼저 확인해볼텐데 잠시만 기다려 주시겠습니까 예예\n네 기다려 주셔서 감사합니다 국민카드로 되어 있으십니다 고객님 아니에요 알 그거를 돈을 낸 바꿔야될거 같아갖고 예전에 일반 신용카드로 등록한다고 인데\n아 그러세요 그러면 지금 그 고객님께서 불러주신 고객님 카드로 등록해드리면 되십니까 아니요 집사람 카드로 했어요 그냥 삼십 만 따로따로 보라그러더라고요 카드번호 말씀해주시면 맞는지 확인해볼게요 예 구 사 사 오 네 사 이 공 구\n오 사 사 오 번에 사 이 공 구 네\n팔 사 삼 팔 아 그 카드로 되어 있지 않으시거든요 고객님 예 그대로 수정 좀 해줬으면 좋겠는데 저희 배우자분하고 동의 통화가 되셔야지만 변경해드릴 수가 있어요 아 그래요 왜냐면 이거를 삼십 만 원 이상 써야\n단말기 값이 거기서 이제 참고 할인된다 해가지고 카드사에서 아 그러면서 배우자분하고 동의 통화 가능하세요 고객님 아니요 그 지금은 아직 티비가 안나오고 있어요 지금 저희가 여섯시까지 상담 가능하시니까요 동있습니까 배우자분께서 직접 연락\n면 아 좀 바꿨으면 좋겠는데 내가 카톡으로 해서 카드를 제가 갖고다니 다 쓰고 있거든 지금 어제 저희가 동의 통화가 되지 않으면 변경하시고 없습니다 고객님\n알겠습니다 그럼 다시 사람한테 전화하라고 할게요 죄송합니다 요거는 인제 드리겠 그건 됐고 이거 요금 아직 청구한것도 안돼서 제가 십 일월 삼일날 개통이 된거라 다음달부터 시작됩니다\n아 그럼 이 카드로 다음달부터 적용되는거에요 죄송하다 이번달 십 이월달부터 시작됩니다 고객님 예 예 알겠습니다 문의사항 있습니까 아닙니다 고맙습니다 감사합니다 케이티 네 이었습니다 네 알겠습니다')
    stt.append('행복을 드리는 브이아이피 전문 상담사 전 하나 입니다\n여보세요 네 여보세요 네 제가 지금 요금제를 변경을 좀 할려고요 아 그러세요 네 제가 정보 확인 후에 얼른 변경처리 좀 도와드리겠습니다\n문의하시는 번호가 공일공 사 둘 오 오 에 칠 삼 삼 일 번 한 미선 고객님 본인 맞습니까 네 업무처리 위해서 추가정보 확인 한가지가 더 필요하신데요 네 등록되어있는 주소 시 서울시 성북구\n그 이하 주소좀 말씀 부탁드립니다 팔 국번이오\n아 이거 그럼 구 공 다시 일 칠 이요 채널 할건데 아 이동 오백 이호요 아 네 고객님 확인해주셔서 감사드립니다 네 그러시면 지금 혹시 따로 생각해두셨던 요금제가 있습니까 고객님\n삼 인가요 삼 삼구요금제인가 뭐\n아 네 저희 엘티이 데이터 선택 요금제중에서 삼 구 구 요금제도 있고요 엘티이 데이터 선택 삼 사 구 요금제도 있습니다 고객님 삼 사 구 가 일기가하고 삼 구 구 가 이기가죠 네 맞습니다 예 삼국으로 해주세요\n네 그러면 지금 말씀해주신 엘티이 데이터 선택 삼 구 구 요금제로 변경을 좀 해드릴텐데요 월정액은 삼만 구천 구백 원에 통화는 지금처럼 통신사 구분없이 유무선 음성통화 무제한으로 적용됩니다\n문자 무제한 그리고 데이터같은 경우에는 이제 이기가바이트로 제공을 해드리게 되세요 네 그리고 오늘 일일자이긴 하지만 혹시라도 이전에 변경하시기 전에 초과사용분 있을 경우에는 초과요금 발생될 수 있\n다라는 거는 청소 한번만 부탁드리겠습니다 지금 엘티이 데이터 선택 삼 구 구 요금제에 대한 유의사항은 제가 문자로 한번 더 전송을 해드리도록 하겠습니다 고객님 음 네 그럼 그게 혹시 넘어갔을때요 네 그게 없나요 아\n문자로 오나요\n네 저희가 전국적으로 네 팔십프로 백프로 소진될때마다 문자로 발송을 해드리고 있습니다 고객님 아 네 네 지금 바로 변경처리는 완료해드려서 지금부터 바로 이용 가능하고요 이제 다른 또 확인해드릴 사항은 없으십니까\n아 고객님 그러면 부가서비스\n그럼 오칠삼구는 건데요 네 지금 부가서비스 여러개 가입되어 있는데 우리 고객님께서 월정액 팔천 원에 알짜팩 플러스라고 하는 저희 가입되어 있고요 그리고 올레 투폰이라고 해서 월정액 사천 원 상품이 남아 가입하실때\n때 초반에 이제 가입이 되었던거 같아요 요거는 네 올레 투폰은 이제 전용 단말기 지금 고객님 그 이용하시는 단말기에서 번호 하나를 더 부여받으셔가지고요 그거\n네 예 저저 있다고요 네 그 두개가 지금 다 가입이 되어있는 상태에요 고객님\n아\n네 그거 해지해주실래요 어 네 그러면 두개 다 해지해드릴까요 아니면 올레 투폰 만 해지를 해드릴까요 고객님 알짜팩을 했을때 뜨지 않고 아 네 아마 가입하셨을때 유지하시라고 아마 가입을 그쪽에서 해주셨\n어떤 거 같아요 이거는 제가 바로 해지를 좀 해드리고 고객님 혹시 단말기 보험도 가입되어 있거든요 그거는 같으세요 보험은 그대로 유지 해드리겠습니다 그럼 날짜\n팩같은 경우에는 제가 지금 해지해 드리게 되면은요 어 알짜팩 플러스 같은 경우에는 일할 계산 되어서 요금 청구가 되시는데 오늘은 일일자라서 요거는 참고해주시면 되시고요 그리고 고객님께서 이제\n알짜팩 플러스는 해지하시고 삼십 일 이내에 재가입이 불가한 상품이세요 혹시라도 뭐 사용은 안하시겠지만 기본 제공 초과 사용분 있다면 추가 요금 발생되실 수 있다라는 것도 참고만 해주시면 되실거\n고요 혹시 그 알짜팩플러스 해지하시게 되면 캐치콜이라던가 링투유 서비스도 함께 해지되시는데 혹시 해당 서비스 필요하시면 따로 가입을 해드릴까요 고객님 어 캐치콜은 그럼 무료 아닌가요 같이 금액이라서요\n캐치콜 이제 문자로 수신 받으시는건데 이제 전화가 꺼져있거나 통화중일 때 못 받으시면 문자로 수신하시는 건데요 예 그거는 월정액 오백 원 따로 부가서비스가\n네 따로 있습니다 고객님 아 오백 원이 있었어요 네 원래 이제 있고 아니시면 뭐 통화중일 때 지금처럼 통화중일때요 다른 분한테 연락을\n네 모두 또 이렇게 통화는 들리면서 이제 바로 이제 받아보실 수 있는거는 무료 서비스라서 뭐 그걸로 해주셔도 되고요 뭐 문자까지 거는 네 그것도 해지가 되는 건가요\n어 그거는 해지되지 않았고요 예 단말기 기능이라서 만약에 혹시 지금 사용안하시고 계시면은 이거는 제가 따로 설정을 좀 해드리면 됩니다 고객님\n네 그건 지금 개인걸로 알고 있는데 해주세요 네 그냥 할려 버리면 네 혹시 모르니까 제가 다시 한번 설정을 좀 해드리고요 그러면은 별도에 더 추가적인 가입없이 알짜팩 플러스 상품이랑 올레 투폰 만 해지해드리면 될까요 고객님\n네네 네 알겠습니다 어 지금 다 처리 완료해드렸는데요 혹시 더 확인해 드릴건데 없으십니까 고객님 아 그럼 제껄로 메일로 바꾸는거 메일 주소 변경은 어디서 해야 돼요\n스마트 요금은요 네 전화상으로도 가능하시고요 이메일 주소 말씀해주시면 바로 수정해드리겠습니다 예 티 에이치 아이 네 예 더 밑에 아래 아이폰 네네 네 아래 아랫 구 칠 삼 삼 하나 네\n골뱅이 네이버 닷컴이오\n네 고객님 제가 혹시 모르니 문자로 한번 더 이 버 이 이메일 주소가 맞는지 한번 문자로 한번 넣어드릴게요 확인한번만 부탁드리겠습니다 네 네 지금 바로 문자 전송해드렸습니다 확인 한번만 부탁드립니다 네\n잠시만요 네\n네 맞아요 네 네 그럼 지금 이메일도 지금 현재 이 이메일 주소로 변경해드려서 다음달부터 아 죄송합니다 이번달부터는 요 변경된 이메일로 해서 청구서도 받아보실 수가 있습니다 고객님 소액결제 한도도 여기서\n조정이 돼요 네 전부 다 가능합니다 예 소액결제 한도 조금만 노트북이 잖아요 네 그럼 한도도 지금 바로 조회 좀 해 드릴텐데요 어 전산을 확인해드려야 되서요 고객님 죄송합니다만 잠시만 기다려 주시겠습니까 네')
    stt.append('행복하세요 케이티 박 슬기 입니다 예 저기 우편물이 지금 저기 케이티\n전화 요금 영수증이 왔는데 요 핸드폰 말씀이십니까 아니요 일반 가게전화 칠백에 공 삼 하나 에 칠 칠 하나 에 네\n구 팔 오 칠 계약자분 성함 말씀해주시겠습니까 김 혜숙\n고객님 본인이십니까 예 네 지금\n양평에서 사용하시는거 맞으시죠 예 맞아요 티비기 어 근데 가게 상호가 안들어가서 우편물을 하시는 분이 이제 그래서 가게 상호를 좀 빨간 전원 좀 넣어주세요\n아 고객님 지금 이게 개인 고객님 명의로 되어있기 때문에 아마 그런거 같고요 그리고요 이거 사업자 네 이거 부가세 혜택을 받을려면 어떻게 해야 돼요 사업자 어떻게 해야 돼요\n부가 사업자 등록해주셔야 되는거 같고요 예 와 다음달에 계약자명과 사업자 대표 등록증상에 대표자명이 동일해야되는데 동일하십니까 예예 네\n네 이 번호에 에다가 신청하시는 거고요 예 사업자 등록증이랑 신청인 신분증 팩스로 보내주셔야지 어디로요 팩스번호 좀 불러 주세요 그럼 공 팔 공 잠깐요 네 공 팔 공 구백 오십 에\n구백 오십 에\n예 팔 팔 영 팔 입니다 팔 팔 영 팔 이요 네 예 아 그러면 여기에다가 요 신분증\n아 신분증이랑 사업자 등록증 보내주시면 되고요 예 신분증은 주민번호 뒷자리 가린 후에 보내주셔야 아 예 사업자 등록증 네네\n예 알았습니다 네 고객 붙으시고 나서 저희쪽에 다시 전화 주셔서 신청해 주시면 되고요 아 네 지금 그러면 빨간 증설이라고 하셨\n네 예예 양근리 지금 주소 되어 있는거에다가 가로치고 빨간 증설이라고 적어 드려도 될까요 예예 네 주소가 지금 양근리 몇번지이십니까\n양근이리\n사백 사백 십 일 다시 십 사 사백 십 일 다시 십사번지 그 가로치고 빨간 부산 부산 죠 예예 그리고 이거 발신자번호 휴대 저기 가게 전화에서 뜨는 것 좀\n신청해 주는데 어떻게 해야 돼요 발신번호표시서비스가 예 였습니다 네\n우선 지금 네 청구지 주소는 그렇게 해가지고선 들어가게 변경해드렸기 때문에 네 다음달부터 그렇게 받으실 수 있을거고요 예예 네 그리고 카드 저기 전화기에 저기\n그 발신자 표시 좀 그것좀 해주세요\n네 발신번호 표시서비스 안내해드릴텐데요 예 예 고객님 부가세 별도로 매월 천 오백 원이 알아요 예 네 그래서 지금 바로 가입해 드릴텐데요 고객님 본인이라고 하셨죠 네 고객님 본인 명의 핸드폰 번호 한번만 말씀해 주시겠\n니까 네 공일공 네\n잠깐요 선이 서류 땜에 공일공 네 사 삼 공 이 사 삼 이 영 둘\n팔 공 오 공 팔 공 오 공 번 고객님 명의 핸드폰 맞으시죠 네 고객님 이 번호로 쪽으로해서 제가 본인 인증 문자 하나 발송해드릴텐데요 예 문자 받으시면 통화버튼 눌러서 에이알에스 멘트만 끝까지 들어주시면 됩니다\n그러면은요 이 전화기를 저희 동생이 쓰거든요 그럼 어떻게 해야돼요 제꺼는 또 스마트폰을 다쓸때 보기는 옛날 전화를\n아 고객님 지금 그 네 사 삼 오 이 에 팔 공 오 공 번이고요 예 제 전화에요 저 전환데 제가 옛날 전화를 그걸 제가 동생이요 스마트 폰을 할지 몰라요 그래서\n그거 갖고 제가 이력에서 오는 일 나갔어요 그리고 내거는 또 스마트폰으로 갖고\n집에서 고객님 본인이라고 하셨는데요 예예 지금 팔 공 오 공 번은 본인 인증 문자 그러면은요 제가요 그러면 거기 인증번호 나오면 은 그 불러드리면 돼요\n이게 고객님 본인 명의 핸드폰이 아닌걸로 확인되기 때문에 문자가 발송이 안되세요\n아\n정하면 예 내일 좀 알았습니다 그러면 이거 전화국에 가서 직접 신청하면 되지요 본인이요 네 아 그러면 그게 낫겠네 그리고 사업자 이것도 가지고 가서 하면 되죠 신분증하고요 같이 신청하셔서\n니다 아 그러면 전신 전화국 가서 할게요 아 네 알겠습니다 더 궁금한 점은 없습니까 예예 수고하세요 네 그럼 제가 따로 처리가 애 였습니다 예예 미소 가득한 하루되세요 케이티 송 다슬 이었습니다 네')
    stt.append('행복을 드리는 케이티 이 지혜 입니다 네 여보세요 네 고객님\n구월 일일부터 사용한 요금 미납된 거 확인 좀 해 주세요 아 그러세요 확인 한번 해보세요 사용하시는 번호가 공일공 팔 구 육 이 에 구 육 일 구 번 맞습니까\n네 명의자분 김 민정 고객님 본인 이시고요 네 아니요 딸이요 아시는 분이세요 그럼 성함 한번 말씀해주시겠습니까\n뭐 선영이요 뭐 사년 고객님이시고 선영이요 논산이요 네 소중한 정보 확인 감사합니다 확인해봤을때 미납요금이 십 사만 삼천 육백 이십 원 이렇게 확인되고 있습니다\n네 상세내역 오월 일일부터 사용한 게 십사만얼마가 나왔다고요 아니요 이제 총 합산된 금액인데 구월일일부터 구월 말일까지 사용하신 미납요금은 칠만 삼천 이백 사십 원\n이렇게 아닙니까 칠만 삼천 이백 삼십 원이요 네 맞습니다 이게 저 기본료와 지금 얼마로 돼있죠\n지금 상세 내역 확인을 위해서 감사 초점 추가 정보 하나만 더 확인해볼텐데 그 접수되어 있는 주소지 구와 동 말씀해주시겠습니까 성북구 돈암 일동 이요 소중한 정보 확인 감사합니다 기본요금이 삼만 구천 구백 원 상품을 현재는\n사용하시고 있네요\n사만 구천 구백 원이요 예 맞습니다 여기가 뭐가 어떻게 나는 칠만얼마가 나온거에요 확인 사만 구천 구백 원이랑 그것도 뭐가 나온거에요 고객님 확인해봤을때 이제 구월달에 칠일 날짜로 구월 칠일 내용 요금제 변경을 한번 하셨어요 제가 구월 칠일날 변경한거에요\n예 삼만 구천 구백 원짜로요 네 옛날에 이제 만 이천 원 상품에서 삼만 네네 이백 원 상품으로 요금제 변경하셨는데 일할 계산이 돼가지고 네 청구요금이 월정액은 사만 이천 삼백 이십 원이 청구가 되고요\n네네 여기 이제 부가서비스 캐치콜 오백 원 네 단말기 할부금이 이만 사천 육백 사십 원 네 그럼 미납요금이 발생이 돼가지고 연체 가산금이 천 오백 십 원이 같이 부과가 되고요\n네 그 요금제로 요금제랑 그 부가서비스에 대한 부가세부가세 금액이\n어 사천 이백 팔십 이 원 이렇게 같이 합산 저거들 해가지고 칠만 삼천 오백 사십 원으로 확인되고 있네요 저 무슨 마지막 모르겠고요 지금 그니까 삼만 구천 구백 원이 요금이 나가고 뭐 날짜 일할계산된다고 잖아요 예 월중간에 요금제 변경하셨으니까요\n그러면 구월 일일부터 육일까지 사용한 요금 따로 부과가 되는 거에요 구월 일일부터 육일까지 그리고 칠일부터 말일까지 사용하신 금액은 일할 계산해가지고 합산해서 시월달 청구 요금으로 청구가 되시는 거세요\n그니까 구월 일일부터 삼십 일까지 사용한거에요 네 맞아요\n그죠 구월 칠일날 이거 요금서 그 이거 이거 변경을 했다면서요 제가 육일치는 이전 요금제에 대한 기본요금이 지금 육일치가 얼마가 나온거에요 따로 계산이 되는거니까 그쵸 계산 한번 해볼텐데 오만 이천 원에 부가세가 원래 오천 이백 원 청구가 되고요\n이제 데이터 이제 구월달이니까 확인 한번 해보겠습니다\n수고하십니다 구월달 구월달 같은 경우에는 삼십 일 로 되어 있었는데 네 큐지 계산해보면 부가세 포함해서 만 천 사백 삼십 구 원 이게 이제 육일칠 청구되는 부분이고요 그럼 칠월 칠일로 바꿨어요 칠일부터 이 요금제로 되는건데\n이것도 일할계산이 되는거에요 제가 바꿨기 때문에 중간에 맞아요\n아 삼만 구천 구백 원 그 요금이 나온게 아니라 예 맞아요 일할 계산 아 그 가입한 날짜계산이 됐던거 다 끝나요 천안 네 맞아요 구월달 그럼 그게 얼마가 나온거예요 그럼 칠일부터 말일까지가 칠일부터 말일까지 같은 경우에는\n삼만 구천 구백 원에 부가세 삼천 구백 구십 원 포함한 금액 중에서 삼십 일 로 나눠서 육일치 빼고 이십 사일치가 삼만 오천 백 십 이월 이렇게 부가세 포함해서 그렇게 다\n그니까 저기 로는 구월 일일부터 육일까지 가 얼마라고요\n다시 한번 발송해 볼게요 오만 이천 원에 부가세 육천 이백 원 포함해가지고 삼십 일 나눠보고 육일치가 부가세 포함해서 만 천 사백 삼십 구 원이고요\n안 이천 사백 삼십 구 원이요 네 만 천 천 사백\n사백 삼십\n구번이요 네 그리고 칠일날 부터 말일까지가 삼 삼만 팔천\n예 삼십 팔 원\n삼만 팔천 삼십 팔 원이요 네 맞습니다\n삼만 팔천 삼만 팔천 삼십 팔 원 이게 부가세 포함 되네 갚어 두개다 구월 일 육 이것도 부가세 포함된 게 만 얼마고 삼십 일 보여줄 삼십 일까지 많은것도 맞나요 삼만 없는게 부가세 포함해서요\n예 맞아요 제가 안내드린건 부가세 포함해서 계산해드린 거세요\n그래서 이것저것 다 이렇게 포함해서 칠만 삼천 이백 삼십 원이 나온거에요 맞습니다 그러면 시월 일일부터 말일까지 사용한거는요 시월 일일부터 말일까지 사용하신 요금이 있으 십 일월달에 원래 청구가 되는데 네네 금액이 칠만 삼백 팔십 원\n이렇게 확인 칠만 삼백 팔십 원이요 네\n이거는 이제 원래 제 요금제 가끔 날짜도 이제 이제 처음부터 나오는 거잖아요 이거는 삼만 구천 구백 원 네 삼만 구천 구백 원 나오고 여기에 부가세가 얼마가 보는 거에요 부가세가 삼천 구백 구백 구십 원 이렇게 아니 그러니까 삼천 구백 원이오\n네 그리고 캐치콜 가입되어 있는것도 오백 원인데 얼마에요 그게 달마다 나가는게 오백 원입니다 콜이 오백 원이요 부가세 오십 원 붙고요\n오백 오십 원이요 예 그것도 뭐가 부터도 여기 연체 가산금이 천 삼백 팔 원이 발생이 되어 있어요 가산금이 천 삼백\n팔월 팔십 아 사만 천 사백 팔월이요 예 또 뭐있어요 단말기 할부금\n포함되어있고요 할부금이 얼마에요 수수료 포함해서 이만 사천 육백 사십 원 확인됩니다 이만 사천\n육백 사십 원이요 네 수수료 포함해서요 맞습니다 그럼 제가 이 할부금은 달마다 똑같이 낮춰도 쓰셔가지고 나오는거죠\n네 그렇죠 연체 가산금을 포함해서 나오는거죠 할부금 네 그러세요 가산금 빼고 그냥 할부금 한건 이만 사천 육백 사십 원 다 나오는 차감되는거에요 맞는데 이 할부금 같은 경우에는 지금\n이제 마지막 납부하시는 달이 다 내년 일월달까지만 납부해주시면 끝나세요 아 내년 일월이요 네\n아 그럼 저희가 이제 할부금 안나온거고요 그래서 내년 일월까지만 납부해주시면 이월달부터 한거 안된다라고 그 여자분 안나오는 거에요 네\n아 이렇게 칠만 삼백 팔십 원이에요 네 칠만 두달치가 합하면 얼마죠 십 사만 삼천 육백 이십 원입니다 사만 삼천\n육백 이십 원이요 네 이게 당월요금이라고 좀 십 이월달 으니까 둘다 미납이 된 거죠 그쵸 그쵸 두달치가 미납이 되는거 되는거죠 네 맞아요\n아 근데 궁금한게 이거 제가 이거 에이알에스 결제할거고요 네 또 궁금한게 제가 카드 핸드폰을 바꾸려고 하는데 기계를 네\n바꾸게 되면은 이 요금제를 그대로 옮겨서 쓸 수도 있는 건가요 가능한데 혹시 변경하실 때 개통 당시에 약정 상품은 이제 가입을 하잖아요 그니까 요 네 근데 그 약정상품\n근데 에스케이는 뭐 바꾸니까 뭐 다른걸로 바꿀수 이거 요금도 쓸수 있다고 말씀을 하셨어요 저번에 상담하셨던 분은 뭐 요금제 같은 경우에는 뭐 개통방식 잠 잠시만요 제가 다시 전화드릴')
    stt.append('행복을 드리는 케이티 이 송이 입니다\n네 그럼 그 한달 휴대폰 바꾼지 한달을 해가지고 네 부가서비스 해지할려고 하는데 해지 좀 해주세요 아 그러세요 네 알겠습니다 문의 번호 공일공 칠 오 이 이 팔 오 구 육 번 신 수한 고객님 명의자 본인 맞습니까\n네 없어요 네 결제중인 납부방법이랑 납부자 성함 말씀해주시겠습니까 어 납부 다고 한거에요 결제하고 있는 납부자 성함이오\n아 인상 하나 결제하고 있는 방법은 카드로 납부하고 있으니까 자동이체로 납부하고 있습니까 아 자동이체요\n자동이체 아닌데요 고객님 아니 카드 카드에요 네 어느 카드사로 납부하고 있습니까\n아 모르겠는데 삼성카드 삼성카드 고맙습니다 현재 단말기 보험 파손형 삼천 이백 원 그 미디어팩 팔천 원 이렇게 두가지 가입되어 있습니다 네\n네 보내드 둘다 해지하시는 거세요 그 두개가 뭐에요 그 하나는\n하나는 보험이고요 한달에 삼기가 팩이라고 해서 패키지 상품이신데 그 올레티비 모바일팩 웹툰 캐치콜 통화가능 알리미 링투유 음원 지니팩 티비포인트가 모두 포함된 패키지 상품입니다\n그게 얼마에요 그게 팔천 원입니다 고객님 월정액 그거 그거 해지해주세요 네 그러면 미디어팩 만 해지해드릴까요\n네 예 월정 해지로 기본료 및 제공 혜택 일할 계산되고 기본 제공량 초과된 부분 있으면 따로 추가로 과금발생 되고요 해지후 당일 재가입 어렵고요\n링투유 부가서비스 해지시 구매하셨던 컨텐츠 보관함 모두 삭제됩니다 혹시 기본팩 캐치콜 링투유 서비스는 따로 신청해드릴까요\n그 무료에요 아 그럼 유료 팔천 이백 원입니다 아\n캐치콜이랑 뭐 한다 그러면 캐치콜만 되는 거에요 그게 캐치콜 링투유 통화연결음 같이 포함된 패키지 상품입니다 원하시면은 그거는 그냥 그것도 안해주셔도 돼요 네 미디어팩 만 해지해드렸습니다\n혹시 아침저녁 기온차가 심합니다 건강 유의하시고요 케이티 이 소연 이였습니다 네 감사합니다 감사합니다 네')
    stt.append('행복을 드리는 케이티 조 경민 입니다\n네 그 다름이 아니라요 제가 그 어머님 핸드폰을 해드렸는데 네 요금이 너무 많이 나왔어요\n네 고객님 그거를 할 수 있나요 네 번호 말씀해 주시면 확인해 보겠습니다 네 공일공 네 육 삼 육 이 육 삼 육 이 에 사 팔 이 칠 이요\n네 명의자분의 성함과 생년월일 말씀해주시겠습니까 김 상덕 이고요 네 팔 공 일 일 이 일\n네 명의자 본인이십니까 인생이요 아 그러세요 네 이 번호를 어머님께서 쓰신다는 말씀이시고요 네\n전화주신 우리 고객님의 성함 말씀해주시겠습니까 김 성철 이요 네 가족분이시고요 네\n네 등록돼있는 주소 구와 동까지만 말씀해주시겠습니까 대야동이요\n대덕구 대화동\n네 확인 감사합니다 고객님 어 지금 이 단말기가 최근에 개통됐다고 하셨는데요 요금을 좀 확인해드릴까요 네 네 개통은 시월 이십 이일 날짜로 개통을 해 주셨고요 네\n네 시월에 이용하셨던 요금이 지난달 청구번호가 되었었는데 칠만 삼천 사백 원으로 청구가 되어 있습니다\n그 왜 그 많이 나왔죠 그게 네 보통 삼만 원 사만 원 뜻이거든요 많이 나가죠\n고객님 잠시 내용 확인해 볼텐데 잠시만 기다려 주시겠습니까 네')
    stt.append('행복을 드리는 케이티 이 나리 입니다 무엇을 도와드릴까요 아 제가 지금 부가서비스 가입되어 있는게 있을텐데 네\n그 무료로 하는 거 말고 요금제는 거면 다 해지할려고 하거든요 아 그러십니까 네네 네 정보 확인후 바로 해지 처리 도와드리겠습니다 문의하시는 번호가 공일공 사\n칠 칠 칠 이 에 이 삼 공 삼 번 이 현성 고객님 명의자분 본인 맞으십니까\n네네 네 등록되어 있는 주소 서울 구로구 집주소 말씀 부탁드립니다 도봉일동 백 삼십 이 다시 칠십 일 오 이백 이호요\n네 전화 정보 확인 정말 감사합니다 네 확인해보니까 고객님께선 지금 미디어팩 가입되어 있으시고요 그거 하나밖에 없죠\n네 그러시고 저희 이제 단말기 보험 가입되어 있으세요 고객님\n아 그거는 근데 또 주시고 네 예 미디어팩만 해지도와드릴까요 네네 그거 말고 다른것도 없죠 네 없으세요 고객님 네네 그럼 미디어팩만 해지할려고요\n아 네 그럼 미디어팩 해지시에는 저희 링투유 서비스도 같이 해지가 되시는데요 링투유나 캐치콜은 별도로 이용하실 수 있는 건 아니시고요 캐치콜 혹시 무료로\n수는 없나요 아 네 죄송합니다만 저희가\n캐치콜 같은 경우는 월 정액 오백 원이십니다 아 아니 아니요 그냥 해지해주세요 아 네 그리고 해지 네 미디어팩 바로 해지하시게 되시면은 해지후 당일 재가입은 불가능하시고요 고객님 네\n네 지금 바로 미디어팩 해지도와드렸습니다 혹시 추가적으로 더 문의하실 내용 있습니까 혹시 제가 지금 십 이월 일일 일일에 해지를 했잖아요 네 그러면 십 이월달 요금에는\n그거에 대한게 안나오고 십 일월까지만 쓴걸로 된 건가요 네 맞으세요 아 네 알겠습니다 아 네 소중한 시간 함께해 주셔서 감사합니다 케이티 이 나림 이였습니다 네\n알겠습니다')
    stt.append('행복을 드리는 케이티 이 한기 입니다 여보세요 네 고객님 네 제가 핸드폰 케이티 썼다가 해지했거든요 네\n근데 그 뭐라그러지 그때 위약금은 다 냈는데 네\n카드 그 저거 뭐지 자동이체로 요금 나가는게 있어가지고요 아 그러세요\n네 그럼 번호 확인해가지고 요거는 뭐 수납된 내용에 청구 내역 확인해드릴 수가 있는데 확인 원하신 핸드폰 번호 한번 말씀해주시겠습니까\n아 번호가 있습니다 가운데번호로 기억이 없는데 어 전화번호 확인을 해야 저희쪽 조회해드릴 수가 있고요 번호를 모르면 조회 자체가 불가능합니다 고객님\n아 그래요 네\n번호를 확인해주셔야 저희쪽도 조회해가지고 해당번호 확인해서 도움드릴수가 있습니다 고객님\n어\n오 육 팔 사\n공일공 오 육 팔 사 에\n어 기억이 없나요\n아니 주민등록번호로도 안돼요 네 주민번호는 조회 자체가 불가능합니다 고객님\n그럼 이걸 어디서 전화가 직접 가서 알아봐야 되나요 아니면 요 번호 확인 같은 경우는 이제 올레 플라자 내방하셔서 가능하고요 명의자분 이시죠 신분증 지점 내방하신 다음에 확인할 수 있습니다 고객님\n아 케이티로요 네 올레플라자 내방하셔가지고는 고객님 직접 확인할 수가 있으신 볼 순 내방하신 다음에\n아 네 알겠습니다 더 플라자 위치 안내 가능한데 안내해드릴까요 네네 네 계신 지역 위치 말씀해주시면 플라자 위치 안내해드리겠습니다\n인천 부평이요 중앙이시고요 네 네 확인해드리겠습니다 잠시만 기다려 주시겠습니까 네\n네 부평쪽에 확인되시는거 확인해봤더니요 네 올레플라자 해가지고요\n뭐 쪽에 확인되시는게요 지금 올레 플라자 부평점 을 해가지고요 조회되는게 있는데요 네 어 이쪽 위치 있는 지역이요 그 상곡동 있죠\n네 올레 플라자 그 산곡동에 보시면은 그 경남상가 있죠\n예 중곡동 밖에 없어요 네 부평쪽에는 산곡동에 있습니다 고객님\n예 산곡동 경남상가 맞은편에 있습니다 고객님께 옆에 그 인천 마산 주더라고요 옆에 있는 걸로 했는데 경남상가 맞은편쪽에 해가지고요\n아\n이게 알겠습니다 네 맞다고 하는데 문자 발송해드릴까요 네네 어 하시면 어느 번호로 문자 발송해드릴까요 아 하나 사 사 네 공 구 오 팔 이요\n네 요청하신 대로 통화중에 문자 발송해 드릴텐데 명의자분 싶으신 봐주셨 내방 하셔가지고 확인가능합니다 네 네 그냥 또는 결제만 이라는 건강 유의하시고요 저는 케이티 이 아름 이었습니다\n아닙니다 네 감사합니다')
    stt.append('행복을 드리는 케이티 김 미정 입니다 여보세요 네 고객님 무엇을 도와드릴까요 어 그 부가서비스 좀 해지할려고 하거든요\n이요 네 확인 후 도움 드리겠습니다 고객님 되어있는\n어 이 구 이 사 칠 육 공 칠 명의자분\n객님 명의자분 본인 맞습니까 아니 저 자녀요 아 그러세요 고객님 네 전화주신분 성함과 연락처 알려주시겠습니까 연락처는 없고 이름은 신규법인이에요\n신규 빈 이요 칠 숫자 비즈 있습니까 네 아 그러세요 고객님 네 되어있는 주소지 인천시 남동구 다음 주소 말씀해\n까 논현동 목포 이백 구십 사 삼십 이동 삼백 일호요\n소중한 정보 확인 감사합니다 우선 제가 조회중에 있습니다 잠시만 기다려 주시겠습니까 네 니다')

    def __init__(self):
        pass

    def getLen(self):
        return len(self.stt)

    def getRandomStt(self):
        # print('>>>', self.getLen() + 1)
        # print('>>>', random.randrange(1, self.getLen() + 1))
        rn = random.randrange(0, self.getLen())
        # print('>>>', rn)
        rStt = self.stt[rn]
        rStt = '#'.join(rStt.split('\n'))
        # rStt = self.stt[random.randrange(1, self.getLen() + 1)]
        # print('>>>', rStt)
        return rStt

