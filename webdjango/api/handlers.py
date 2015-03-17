from piston.handler import BaseHandler

from evaluator.usecases.answer_evaluation_form import DataStructure
from webdjango.factories import create_async_evaluation_form_usecase


class EvaluationFormHandler(BaseHandler):
    methods_allowed = ('POST',)

    def create(self, request):
        form = request.POST.dict()

        evaluation_form = DataStructure(
            name=form.get('name'),
            email=form.get('email'),
            html_skill=form.get('html'),
            css_skill=form.get('css'),
            javascript_skill=form.get('javascript'),
            python_skill=form.get('python'),
            django_skill=form.get('django'),
            ios_skill=form.get('ios'),
            android_skill=form.get('android')
        )

        usecase = create_async_evaluation_form_usecase()
        response = usecase.execute(evaluation_form)
        return response