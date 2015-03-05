from piston.handler import BaseHandler
from evaluator.usecases.answer_evaluation_form import EvaluationForm, AnswerEvaluationFormUseCase
from parsers import SafeForm
from webdjango.email import DjangoAsyncEmailGateway


class EvaluationFormHandler(BaseHandler):
    methods_allowed = ('GET',)

    def read(self, request):
        form = SafeForm(request.POST.dict())

        evaluation_form = EvaluationForm(form.str('name'), form.str('email'), skills={
            'html': form.int('html'),
            'css': form.int('css'),
            'javascript': form.int('javascript'),
            'python': form.int('python'),
            'django': form.int('django'),
            'android': form.int('android'),
            'ios': form.int('ios'),
            })

        return AnswerEvaluationFormUseCase(DjangoAsyncEmailGateway()).execute(evaluation_form)