from datetime import datetime, timedelta

from django.test import TestCase
from django.utils import timezone
from django.urls import reverse

from .models import Question
from .utils import summarize

def create_question(question_text, days):
    """
    Create a question with the given `question_text` and published the
    given number of `days` offset to now (negative for questions published
    in the past, positive for questions that have yet to be published).
    """
    time = timezone.now() + timedelta(days=days)
    return Question.objects.create(question_text=question_text, pub_date=time)

class QuestionModelTests(TestCase):

    def test_was_published_recently_with_old_question(self):
        """
        was_published_recently() returns False for questions whose pub_date
        is older than 1 day.
        """
        # time = timezone.now() - datetime.timedelta(days=1, seconds=1)   # python 2
        time = timezone.now() - timedelta(days=1, seconds=1) # python 3
        old_question = Question(pub_date=time)
        self.assertIs(old_question.was_published_recently(), False)

    def test_was_published_recently_with_recent_question(self):
        """
        was_published_recently() returns True for questions whose pub_date
        is within the last day.
        """
        # time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)    # python 2
        time = timezone.now() - timedelta(hours=23, minutes=59, seconds=59)    # python 3
        recent_question = Question(pub_date=time)
        self.assertIs(recent_question.was_published_recently(), True)

    def test_was_published_recently_with_future_question(self):
        """
        was_published_recently() returns False for questions whose pub_date
        is in the future.
        """
        # time = timezone.now() + datetime.timedelta(days=30)   # python 2
        time = timezone.now() + timedelta(days=30) # python 3
        future_question = Question(pub_date=time)
        self.assertIs(future_question.was_published_recently(), False)

    def test_no_questions(self):
        """
        If no questions exist, an appropriate message is displayed.
        """
        response = self.client.get(reverse('polls:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No polls are available.")
        self.assertQuerysetEqual(response.context['latest_question_list'], [])

    def test_past_question(self):
        """
        Questions with a pub_date in the past are displayed on the
        index page.
        """
        create_question(question_text="Past question.", days=-30)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(
            response.context['latest_question_list'],
            ['<Question: Past question.>']
        )

    def test_future_question(self):
        """
        Questions with a pub_date in the future aren't displayed on
        the index page.
        """
        create_question(question_text="Future question.", days=30)
        response = self.client.get(reverse('polls:index'))
        self.assertContains(response, "No polls are available.")
        self.assertQuerysetEqual(response.context['latest_question_list'], [])

    def test_future_question_and_past_question(self):
        """
        Even if both past and future questions exist, only past questions
        are displayed.
        """
        create_question(question_text="Past question.", days=-30)
        create_question(question_text="Future question.", days=30)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(
            response.context['latest_question_list'],
            ['<Question: Past question.>']
        )

    def test_two_past_questions(self):
        """
        The questions index page may display multiple questions.
        """
        create_question(question_text="Past question 1.", days=-30)
        create_question(question_text="Past question 2.", days=-5)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(
            response.context['latest_question_list'],
            ['<Question: Past question 2.>', '<Question: Past question 1.>']
        )

class QuestionDetailViewTests(TestCase):

    def test_future_question(self):
        """
        The detail view of a question with a pub_date in the future
        returns a 404 not found.
        """
        future_question = create_question(question_text='Future question.', days=5)
        url = reverse('polls:detail', args=(future_question.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_past_question(self):
        """
        The detail view of a question with a pub_date in the past
        displays the question's text.
        """
        past_question = create_question(question_text='Past Question.', days=-5)
        url = reverse('polls:detail', args=(past_question.id,))
        response = self.client.get(url)
        self.assertContains(response, past_question.question_text)

class SummarizeViewTests(TestCase):
    def test_summarize_view(self):
        """

        """
        url = reverse('polls:summarize')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_summarize_proc(self):
        """

        """
        context = "자유한국당, 바른미래당, 민주평화당, 정의당 등 야 4당이 20일 공공기관 채용비리에 대한 국정조사를 공식 요구했다. 특히 조명래 환경부 장관 임명에 대한 문재인 대통령의 사과, 조국 민정수석 경질, 채용비리 국정조사를 요구하며 국회 일정을 거부 중인 한국당과 바른미래당은 국정조사만 수용되면 국회를 정상화하겠다고 했다. 여당인 더불어민주당은 당내 여론을 수렴해 야당이 협상안으로 내놓은 ‘국정조사 실시-국회 정상화’ 방안의 수용 여부를 결정키로 했다. 이에 따라 민주당의 결정이 예산국회 정상화의 분수령이 될 것으로 보인다. 민주당 홍영표, 한국당 김성태, 바른미래당 김관영, 평화당 장병완, 정의당 윤소하 원내대표 등 여야 5당 원내대표는 이날 국회에서 문희상 국회의장 주재로 회동을 갖고 국회 정상화 방안을 논의했다. 야 4당은 서울교통공사의 고용세습 의혹과 강원랜드 채용비리 의혹을 함께 조사하는 국정조사 수용을 여당에 요구했다. 한국당, 바른미래당은 여당이 국정조사 요구를 수용하면 국회를 정상화하겠다는 뜻을 전했다. 문 의장도 야 4당의 요구가 있는 만큼 조속한 국회 정상화를 위해 여야가 합의해야 한다고 종용한 것으로 알려졌다. 예산안 심사를 앞두고 멈춰 선 국회를 정상화하기 위해 여당이 대승적으로 국정조사를 수용할 필요가 있다는 뜻을 에둘러 전달한 것이라는 해석이 나온다."

        summarize_result = summarize.TextRank(context).summarize()

        compare = "자유한국당, 바른미래당, 민주평화당, 정의당 등 야 4당이 20일 공공기관 채용비리에 대한 국정조사를 공식 요구했다.\n 야 4당은 서울교통공사의 고용세습 의혹과 강원랜드 채용비리 의혹을 함께 조사하는 국정조사 수용을 여당에 요구했다.\n 한국당, 바른미래당은 여당이 국정조사 요구를 수용하면 국회를 정상화하겠다는 뜻을 전했다."

        self.assertEqual(summarize_result, compare)
