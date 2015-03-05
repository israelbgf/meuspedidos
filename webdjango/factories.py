from evaluator.usecases.answer_evaluation_form import AnswerEvaluationFormUseCase
from webdjango.gateways.email import DjangoSyncEmailGateway, DjangoAsyncEmailGateway
from webdjango.gateways.test import PersistenceGateway


def create_sync_evaluation_form_usecase():
    return AnswerEvaluationFormUseCase(DjangoSyncEmailGateway(), PersistenceGateway())


def create_async_evaluation_form_usecase():
    return AnswerEvaluationFormUseCase(DjangoAsyncEmailGateway(), PersistenceGateway())