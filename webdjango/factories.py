from evaluator.usecases.answer_evaluation_form import AnswerEvaluationFormUseCase
from webdjango.gateways.email import DjangoSyncEmailGateway, DjangoAsyncEmailGateway
from webdjango.gateways.persistence import EvaluationFormGateway


def create_sync_evaluation_form_usecase():
    return AnswerEvaluationFormUseCase(DjangoSyncEmailGateway(), EvaluationFormGateway())


def create_async_evaluation_form_usecase():
    return AnswerEvaluationFormUseCase(DjangoAsyncEmailGateway(), EvaluationFormGateway())