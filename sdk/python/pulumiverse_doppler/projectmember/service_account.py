# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['ServiceAccountArgs', 'ServiceAccount']

@pulumi.input_type
class ServiceAccountArgs:
    def __init__(__self__, *,
                 project: pulumi.Input[str],
                 role: pulumi.Input[str],
                 service_account_slug: pulumi.Input[str],
                 environments: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a ServiceAccount resource.
        :param pulumi.Input[str] project: The name of the Doppler project where the access is applied
        :param pulumi.Input[str] role: The project role identifier for the access
        :param pulumi.Input[str] service_account_slug: The slug of the Doppler service account
        :param pulumi.Input[Sequence[pulumi.Input[str]]] environments: The environments in the project where this access will apply (null or omitted for roles with access to all environments)
        """
        pulumi.set(__self__, "project", project)
        pulumi.set(__self__, "role", role)
        pulumi.set(__self__, "service_account_slug", service_account_slug)
        if environments is not None:
            pulumi.set(__self__, "environments", environments)

    @property
    @pulumi.getter
    def project(self) -> pulumi.Input[str]:
        """
        The name of the Doppler project where the access is applied
        """
        return pulumi.get(self, "project")

    @project.setter
    def project(self, value: pulumi.Input[str]):
        pulumi.set(self, "project", value)

    @property
    @pulumi.getter
    def role(self) -> pulumi.Input[str]:
        """
        The project role identifier for the access
        """
        return pulumi.get(self, "role")

    @role.setter
    def role(self, value: pulumi.Input[str]):
        pulumi.set(self, "role", value)

    @property
    @pulumi.getter(name="serviceAccountSlug")
    def service_account_slug(self) -> pulumi.Input[str]:
        """
        The slug of the Doppler service account
        """
        return pulumi.get(self, "service_account_slug")

    @service_account_slug.setter
    def service_account_slug(self, value: pulumi.Input[str]):
        pulumi.set(self, "service_account_slug", value)

    @property
    @pulumi.getter
    def environments(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        The environments in the project where this access will apply (null or omitted for roles with access to all environments)
        """
        return pulumi.get(self, "environments")

    @environments.setter
    def environments(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "environments", value)


@pulumi.input_type
class _ServiceAccountState:
    def __init__(__self__, *,
                 environments: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 role: Optional[pulumi.Input[str]] = None,
                 service_account_slug: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering ServiceAccount resources.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] environments: The environments in the project where this access will apply (null or omitted for roles with access to all environments)
        :param pulumi.Input[str] project: The name of the Doppler project where the access is applied
        :param pulumi.Input[str] role: The project role identifier for the access
        :param pulumi.Input[str] service_account_slug: The slug of the Doppler service account
        """
        if environments is not None:
            pulumi.set(__self__, "environments", environments)
        if project is not None:
            pulumi.set(__self__, "project", project)
        if role is not None:
            pulumi.set(__self__, "role", role)
        if service_account_slug is not None:
            pulumi.set(__self__, "service_account_slug", service_account_slug)

    @property
    @pulumi.getter
    def environments(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        The environments in the project where this access will apply (null or omitted for roles with access to all environments)
        """
        return pulumi.get(self, "environments")

    @environments.setter
    def environments(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "environments", value)

    @property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the Doppler project where the access is applied
        """
        return pulumi.get(self, "project")

    @project.setter
    def project(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "project", value)

    @property
    @pulumi.getter
    def role(self) -> Optional[pulumi.Input[str]]:
        """
        The project role identifier for the access
        """
        return pulumi.get(self, "role")

    @role.setter
    def role(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "role", value)

    @property
    @pulumi.getter(name="serviceAccountSlug")
    def service_account_slug(self) -> Optional[pulumi.Input[str]]:
        """
        The slug of the Doppler service account
        """
        return pulumi.get(self, "service_account_slug")

    @service_account_slug.setter
    def service_account_slug(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "service_account_slug", value)


class ServiceAccount(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 environments: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 role: Optional[pulumi.Input[str]] = None,
                 service_account_slug: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Manage a Doppler project service account member.

        ## Example Usage

        ```python
        import pulumi
        import pulumiverse_doppler as doppler

        backend_ci = doppler.project_member.ServiceAccount("backend_ci",
            project="backend",
            service_account_slug=ci["slug"],
            role="viewer",
            environments=[
                "dev",
                "stg",
                "prd",
            ])
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] environments: The environments in the project where this access will apply (null or omitted for roles with access to all environments)
        :param pulumi.Input[str] project: The name of the Doppler project where the access is applied
        :param pulumi.Input[str] role: The project role identifier for the access
        :param pulumi.Input[str] service_account_slug: The slug of the Doppler service account
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ServiceAccountArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Manage a Doppler project service account member.

        ## Example Usage

        ```python
        import pulumi
        import pulumiverse_doppler as doppler

        backend_ci = doppler.project_member.ServiceAccount("backend_ci",
            project="backend",
            service_account_slug=ci["slug"],
            role="viewer",
            environments=[
                "dev",
                "stg",
                "prd",
            ])
        ```

        :param str resource_name: The name of the resource.
        :param ServiceAccountArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ServiceAccountArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 environments: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 role: Optional[pulumi.Input[str]] = None,
                 service_account_slug: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ServiceAccountArgs.__new__(ServiceAccountArgs)

            __props__.__dict__["environments"] = environments
            if project is None and not opts.urn:
                raise TypeError("Missing required property 'project'")
            __props__.__dict__["project"] = project
            if role is None and not opts.urn:
                raise TypeError("Missing required property 'role'")
            __props__.__dict__["role"] = role
            if service_account_slug is None and not opts.urn:
                raise TypeError("Missing required property 'service_account_slug'")
            __props__.__dict__["service_account_slug"] = service_account_slug
        super(ServiceAccount, __self__).__init__(
            'doppler:projectMember/serviceAccount:ServiceAccount',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            environments: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            project: Optional[pulumi.Input[str]] = None,
            role: Optional[pulumi.Input[str]] = None,
            service_account_slug: Optional[pulumi.Input[str]] = None) -> 'ServiceAccount':
        """
        Get an existing ServiceAccount resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] environments: The environments in the project where this access will apply (null or omitted for roles with access to all environments)
        :param pulumi.Input[str] project: The name of the Doppler project where the access is applied
        :param pulumi.Input[str] role: The project role identifier for the access
        :param pulumi.Input[str] service_account_slug: The slug of the Doppler service account
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _ServiceAccountState.__new__(_ServiceAccountState)

        __props__.__dict__["environments"] = environments
        __props__.__dict__["project"] = project
        __props__.__dict__["role"] = role
        __props__.__dict__["service_account_slug"] = service_account_slug
        return ServiceAccount(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def environments(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        The environments in the project where this access will apply (null or omitted for roles with access to all environments)
        """
        return pulumi.get(self, "environments")

    @property
    @pulumi.getter
    def project(self) -> pulumi.Output[str]:
        """
        The name of the Doppler project where the access is applied
        """
        return pulumi.get(self, "project")

    @property
    @pulumi.getter
    def role(self) -> pulumi.Output[str]:
        """
        The project role identifier for the access
        """
        return pulumi.get(self, "role")

    @property
    @pulumi.getter(name="serviceAccountSlug")
    def service_account_slug(self) -> pulumi.Output[str]:
        """
        The slug of the Doppler service account
        """
        return pulumi.get(self, "service_account_slug")

