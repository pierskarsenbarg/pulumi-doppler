# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['BranchConfigArgs', 'BranchConfig']

@pulumi.input_type
class BranchConfigArgs:
    def __init__(__self__, *,
                 environment: pulumi.Input[str],
                 name: pulumi.Input[str],
                 project: pulumi.Input[str]):
        """
        The set of arguments for constructing a BranchConfig resource.
        :param pulumi.Input[str] environment: The name of the Doppler environment where the config is located
        :param pulumi.Input[str] name: The name of the Doppler config
        :param pulumi.Input[str] project: The name of the Doppler project where the config is located
        """
        pulumi.set(__self__, "environment", environment)
        pulumi.set(__self__, "name", name)
        pulumi.set(__self__, "project", project)

    @property
    @pulumi.getter
    def environment(self) -> pulumi.Input[str]:
        """
        The name of the Doppler environment where the config is located
        """
        return pulumi.get(self, "environment")

    @environment.setter
    def environment(self, value: pulumi.Input[str]):
        pulumi.set(self, "environment", value)

    @property
    @pulumi.getter
    def name(self) -> pulumi.Input[str]:
        """
        The name of the Doppler config
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: pulumi.Input[str]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def project(self) -> pulumi.Input[str]:
        """
        The name of the Doppler project where the config is located
        """
        return pulumi.get(self, "project")

    @project.setter
    def project(self, value: pulumi.Input[str]):
        pulumi.set(self, "project", value)


@pulumi.input_type
class _BranchConfigState:
    def __init__(__self__, *,
                 environment: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering BranchConfig resources.
        :param pulumi.Input[str] environment: The name of the Doppler environment where the config is located
        :param pulumi.Input[str] name: The name of the Doppler config
        :param pulumi.Input[str] project: The name of the Doppler project where the config is located
        """
        if environment is not None:
            pulumi.set(__self__, "environment", environment)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if project is not None:
            pulumi.set(__self__, "project", project)

    @property
    @pulumi.getter
    def environment(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the Doppler environment where the config is located
        """
        return pulumi.get(self, "environment")

    @environment.setter
    def environment(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "environment", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the Doppler config
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the Doppler project where the config is located
        """
        return pulumi.get(self, "project")

    @project.setter
    def project(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "project", value)


class BranchConfig(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 environment: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Manage a Doppler config.

        ## Example Usage

        ```python
        import pulumi
        import pulumiverse_doppler as doppler

        backend_ci_github = doppler.BranchConfig("backendCiGithub",
            environment="ci",
            name="ci_github",
            project="backend")
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] environment: The name of the Doppler environment where the config is located
        :param pulumi.Input[str] name: The name of the Doppler config
        :param pulumi.Input[str] project: The name of the Doppler project where the config is located
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: BranchConfigArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Manage a Doppler config.

        ## Example Usage

        ```python
        import pulumi
        import pulumiverse_doppler as doppler

        backend_ci_github = doppler.BranchConfig("backendCiGithub",
            environment="ci",
            name="ci_github",
            project="backend")
        ```

        :param str resource_name: The name of the resource.
        :param BranchConfigArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(BranchConfigArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 environment: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = BranchConfigArgs.__new__(BranchConfigArgs)

            if environment is None and not opts.urn:
                raise TypeError("Missing required property 'environment'")
            __props__.__dict__["environment"] = environment
            if name is None and not opts.urn:
                raise TypeError("Missing required property 'name'")
            __props__.__dict__["name"] = name
            if project is None and not opts.urn:
                raise TypeError("Missing required property 'project'")
            __props__.__dict__["project"] = project
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="doppler:index/config:Config")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(BranchConfig, __self__).__init__(
            'doppler:index/branchConfig:BranchConfig',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            environment: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            project: Optional[pulumi.Input[str]] = None) -> 'BranchConfig':
        """
        Get an existing BranchConfig resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] environment: The name of the Doppler environment where the config is located
        :param pulumi.Input[str] name: The name of the Doppler config
        :param pulumi.Input[str] project: The name of the Doppler project where the config is located
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _BranchConfigState.__new__(_BranchConfigState)

        __props__.__dict__["environment"] = environment
        __props__.__dict__["name"] = name
        __props__.__dict__["project"] = project
        return BranchConfig(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def environment(self) -> pulumi.Output[str]:
        """
        The name of the Doppler environment where the config is located
        """
        return pulumi.get(self, "environment")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the Doppler config
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def project(self) -> pulumi.Output[str]:
        """
        The name of the Doppler project where the config is located
        """
        return pulumi.get(self, "project")

