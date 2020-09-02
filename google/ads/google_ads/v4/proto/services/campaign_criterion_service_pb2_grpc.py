# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from google.ads.google_ads.v4.proto.resources import campaign_criterion_pb2 as google_dot_ads_dot_googleads__v4_dot_proto_dot_resources_dot_campaign__criterion__pb2
from google.ads.google_ads.v4.proto.services import campaign_criterion_service_pb2 as google_dot_ads_dot_googleads__v4_dot_proto_dot_services_dot_campaign__criterion__service__pb2


class CampaignCriterionServiceStub(object):
  """Proto file describing the Campaign Criterion service.

  Service to manage campaign criteria.
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.GetCampaignCriterion = channel.unary_unary(
        '/google.ads.googleads.v4.services.CampaignCriterionService/GetCampaignCriterion',
        request_serializer=google_dot_ads_dot_googleads__v4_dot_proto_dot_services_dot_campaign__criterion__service__pb2.GetCampaignCriterionRequest.SerializeToString,
        response_deserializer=google_dot_ads_dot_googleads__v4_dot_proto_dot_resources_dot_campaign__criterion__pb2.CampaignCriterion.FromString,
        )
    self.MutateCampaignCriteria = channel.unary_unary(
        '/google.ads.googleads.v4.services.CampaignCriterionService/MutateCampaignCriteria',
        request_serializer=google_dot_ads_dot_googleads__v4_dot_proto_dot_services_dot_campaign__criterion__service__pb2.MutateCampaignCriteriaRequest.SerializeToString,
        response_deserializer=google_dot_ads_dot_googleads__v4_dot_proto_dot_services_dot_campaign__criterion__service__pb2.MutateCampaignCriteriaResponse.FromString,
        )


class CampaignCriterionServiceServicer(object):
  """Proto file describing the Campaign Criterion service.

  Service to manage campaign criteria.
  """

  def GetCampaignCriterion(self, request, context):
    """Returns the requested criterion in full detail.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def MutateCampaignCriteria(self, request, context):
    """Creates, updates, or removes criteria. Operation statuses are returned.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_CampaignCriterionServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'GetCampaignCriterion': grpc.unary_unary_rpc_method_handler(
          servicer.GetCampaignCriterion,
          request_deserializer=google_dot_ads_dot_googleads__v4_dot_proto_dot_services_dot_campaign__criterion__service__pb2.GetCampaignCriterionRequest.FromString,
          response_serializer=google_dot_ads_dot_googleads__v4_dot_proto_dot_resources_dot_campaign__criterion__pb2.CampaignCriterion.SerializeToString,
      ),
      'MutateCampaignCriteria': grpc.unary_unary_rpc_method_handler(
          servicer.MutateCampaignCriteria,
          request_deserializer=google_dot_ads_dot_googleads__v4_dot_proto_dot_services_dot_campaign__criterion__service__pb2.MutateCampaignCriteriaRequest.FromString,
          response_serializer=google_dot_ads_dot_googleads__v4_dot_proto_dot_services_dot_campaign__criterion__service__pb2.MutateCampaignCriteriaResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'google.ads.googleads.v4.services.CampaignCriterionService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))