# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['SecretArgs', 'Secret']

@pulumi.input_type
class SecretArgs:
    def __init__(__self__, *,
                 config: pulumi.Input[str],
                 name: pulumi.Input[str],
                 project: pulumi.Input[str],
                 value: pulumi.Input[str]):
        """
        The set of arguments for constructing a Secret resource.
        :param pulumi.Input[str] config: The name of the Doppler config
        :param pulumi.Input[str] name: The name of the Doppler secret
        :param pulumi.Input[str] project: The name of the Doppler project
        :param pulumi.Input[str] value: The raw secret value
        """
        pulumi.set(__self__, "config", config)
        pulumi.set(__self__, "name", name)
        pulumi.set(__self__, "project", project)
        pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter
    def config(self) -> pulumi.Input[str]:
        """
        The name of the Doppler config
        """
        return pulumi.get(self, "config")

    @config.setter
    def config(self, value: pulumi.Input[str]):
        pulumi.set(self, "config", value)

    @property
    @pulumi.getter
    def name(self) -> pulumi.Input[str]:
        """
        The name of the Doppler secret
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: pulumi.Input[str]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def project(self) -> pulumi.Input[str]:
        """
        The name of the Doppler project
        """
        return pulumi.get(self, "project")

    @project.setter
    def project(self, value: pulumi.Input[str]):
        pulumi.set(self, "project", value)

    @property
    @pulumi.getter
    def value(self) -> pulumi.Input[str]:
        """
        The raw secret value
        """
        return pulumi.get(self, "value")

    @value.setter
    def value(self, value: pulumi.Input[str]):
        pulumi.set(self, "value", value)


@pulumi.input_type
class _SecretState:
    def __init__(__self__, *,
                 computed: Optional[pulumi.Input[str]] = None,
                 config: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 value: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering Secret resources.
        :param pulumi.Input[str] computed: The computed secret value, after resolving secret references
        :param pulumi.Input[str] config: The name of the Doppler config
        :param pulumi.Input[str] name: The name of the Doppler secret
        :param pulumi.Input[str] project: The name of the Doppler project
        :param pulumi.Input[str] value: The raw secret value
        """
        if computed is not None:
            pulumi.set(__self__, "computed", computed)
        if config is not None:
            pulumi.set(__self__, "config", config)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if project is not None:
            pulumi.set(__self__, "project", project)
        if value is not None:
            pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter
    def computed(self) -> Optional[pulumi.Input[str]]:
        """
        The computed secret value, after resolving secret references
        """
        return pulumi.get(self, "computed")

    @computed.setter
    def computed(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "computed", value)

    @property
    @pulumi.getter
    def config(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the Doppler config
        """
        return pulumi.get(self, "config")

    @config.setter
    def config(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "config", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the Doppler secret
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the Doppler project
        """
        return pulumi.get(self, "project")

    @project.setter
    def project(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "project", value)

    @property
    @pulumi.getter
    def value(self) -> Optional[pulumi.Input[str]]:
        """
        The raw secret value
        """
        return pulumi.get(self, "value")

    @value.setter
    def value(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "value", value)


class Secret(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 config: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 value: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Manage a single Doppler secret in a config.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] config: The name of the Doppler config
        :param pulumi.Input[str] name: The name of the Doppler secret
        :param pulumi.Input[str] project: The name of the Doppler project
        :param pulumi.Input[str] value: The raw secret value
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: SecretArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Manage a single Doppler secret in a config.

        :param str resource_name: The name of the resource.
        :param SecretArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(SecretArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 config: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 value: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = SecretArgs.__new__(SecretArgs)

            if config is None and not opts.urn:
                raise TypeError("Missing required property 'config'")
            __props__.__dict__["config"] = config
            if name is None and not opts.urn:
                raise TypeError("Missing required property 'name'")
            __props__.__dict__["name"] = name
            if project is None and not opts.urn:
                raise TypeError("Missing required property 'project'")
            __props__.__dict__["project"] = project
            if value is None and not opts.urn:
                raise TypeError("Missing required property 'value'")
            __props__.__dict__["value"] = None if value is None else pulumi.Output.secret(value)
            __props__.__dict__["computed"] = None
        secret_opts = pulumi.ResourceOptions(additional_secret_outputs=["computed", "value"])
        opts = pulumi.ResourceOptions.merge(opts, secret_opts)
        super(Secret, __self__).__init__(
            'doppler:index/secret:Secret',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            computed: Optional[pulumi.Input[str]] = None,
            config: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            project: Optional[pulumi.Input[str]] = None,
            value: Optional[pulumi.Input[str]] = None) -> 'Secret':
        """
        Get an existing Secret resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] computed: The computed secret value, after resolving secret references
        :param pulumi.Input[str] config: The name of the Doppler config
        :param pulumi.Input[str] name: The name of the Doppler secret
        :param pulumi.Input[str] project: The name of the Doppler project
        :param pulumi.Input[str] value: The raw secret value
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _SecretState.__new__(_SecretState)

        __props__.__dict__["computed"] = computed
        __props__.__dict__["config"] = config
        __props__.__dict__["name"] = name
        __props__.__dict__["project"] = project
        __props__.__dict__["value"] = value
        return Secret(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def computed(self) -> pulumi.Output[str]:
        """
        The computed secret value, after resolving secret references
        """
        return pulumi.get(self, "computed")

    @property
    @pulumi.getter
    def config(self) -> pulumi.Output[str]:
        """
        The name of the Doppler config
        """
        return pulumi.get(self, "config")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the Doppler secret
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def project(self) -> pulumi.Output[str]:
        """
        The name of the Doppler project
        """
        return pulumi.get(self, "project")

    @property
    @pulumi.getter
    def value(self) -> pulumi.Output[str]:
        """
        The raw secret value
        """
        return pulumi.get(self, "value")

