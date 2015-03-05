from piston.handler import BaseHandler

from evaluator.usecases.answer_evaluation_form import EvaluationForm, AnswerEvaluationFormUseCase
from parsers import SafeForm
from webdjango.factories import create_async_evaluation_form_usecase
from webdjango.gateways.email import DjangoAsyncEmailGateway


class EvaluationFormHandler(BaseHandler):
    methods_allowed = ('POST',)

    def create(self, request):
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

        usecase = create_async_evaluation_form_usecase()
        response = usecase.execute(evaluation_form)
        return response