from grpc.aio import ServicerContext

from protos.gen.contracts.services.payments.payments_service_pb2_grpc import PaymentsServiceServicer
from services.payments.apps.payments.api.mock import loader

from protos.gen.contracts.services.payments.rpc_authorize_payment_pb2 import (

    AuthorizePaymentResponse,
    AuthorizePaymentRequest
)
from protos.gen.contracts.services.payments.rpc_capture_payment_pb2 import (
    CapturePaymentResponse,
    CapturePaymentRequest
)
from protos.gen.contracts.services.payments.rpc_refund_payment_pb2 import (
    RefundPaymentResponse,
    RefundPaymentRequest
)


class PaymentsMockService(PaymentsServiceServicer):

    async def RefundPayment(self, request: RefundPaymentRequest, context: ServicerContext) -> RefundPaymentResponse:
        return await loader.load_grpc_with_timeout(
            "RefundPayment/default.json",  # путь к JSON-файлу с ответом
            RefundPaymentResponse  # схема ответа
        )

    async def CapturePayment(self, request: CapturePaymentRequest, context: ServicerContext) -> CapturePaymentResponse:
        """
        Обрабатывает запрос на подтверждение платежа.
        """
        return await loader.load_grpc_with_timeout(
            "CapturePayment/default.json",
            CapturePaymentResponse
        )

    async def AuthorizePayment(self, request: AuthorizePaymentRequest,
                               context: ServicerContext) -> AuthorizePaymentResponse:
        """
        Обрабатывает запрос авторизации платежа по карте.
        """
        return await loader.load_grpc_with_timeout(
            "AuthorizePayment/default.json",
            AuthorizePaymentResponse
        )
