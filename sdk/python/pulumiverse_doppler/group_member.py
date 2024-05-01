# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['GroupMemberArgs', 'GroupMember']

@pulumi.input_type
class GroupMemberArgs:
    def __init__(__self__, *,
                 group_slug: pulumi.Input[str],
                 user_slug: pulumi.Input[str]):
        """
        The set of arguments for constructing a GroupMember resource.
        :param pulumi.Input[str] group_slug: The slug of the Doppler group
        :param pulumi.Input[str] user_slug: The slug of the Doppler workplace user
        """
        pulumi.set(__self__, "group_slug", group_slug)
        pulumi.set(__self__, "user_slug", user_slug)

    @property
    @pulumi.getter(name="groupSlug")
    def group_slug(self) -> pulumi.Input[str]:
        """
        The slug of the Doppler group
        """
        return pulumi.get(self, "group_slug")

    @group_slug.setter
    def group_slug(self, value: pulumi.Input[str]):
        pulumi.set(self, "group_slug", value)

    @property
    @pulumi.getter(name="userSlug")
    def user_slug(self) -> pulumi.Input[str]:
        """
        The slug of the Doppler workplace user
        """
        return pulumi.get(self, "user_slug")

    @user_slug.setter
    def user_slug(self, value: pulumi.Input[str]):
        pulumi.set(self, "user_slug", value)


@pulumi.input_type
class _GroupMemberState:
    def __init__(__self__, *,
                 group_slug: Optional[pulumi.Input[str]] = None,
                 user_slug: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering GroupMember resources.
        :param pulumi.Input[str] group_slug: The slug of the Doppler group
        :param pulumi.Input[str] user_slug: The slug of the Doppler workplace user
        """
        if group_slug is not None:
            pulumi.set(__self__, "group_slug", group_slug)
        if user_slug is not None:
            pulumi.set(__self__, "user_slug", user_slug)

    @property
    @pulumi.getter(name="groupSlug")
    def group_slug(self) -> Optional[pulumi.Input[str]]:
        """
        The slug of the Doppler group
        """
        return pulumi.get(self, "group_slug")

    @group_slug.setter
    def group_slug(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "group_slug", value)

    @property
    @pulumi.getter(name="userSlug")
    def user_slug(self) -> Optional[pulumi.Input[str]]:
        """
        The slug of the Doppler workplace user
        """
        return pulumi.get(self, "user_slug")

    @user_slug.setter
    def user_slug(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "user_slug", value)


class GroupMember(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 group_slug: Optional[pulumi.Input[str]] = None,
                 user_slug: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Manage a Doppler user/group membership.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] group_slug: The slug of the Doppler group
        :param pulumi.Input[str] user_slug: The slug of the Doppler workplace user
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: GroupMemberArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Manage a Doppler user/group membership.

        :param str resource_name: The name of the resource.
        :param GroupMemberArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(GroupMemberArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 group_slug: Optional[pulumi.Input[str]] = None,
                 user_slug: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = GroupMemberArgs.__new__(GroupMemberArgs)

            if group_slug is None and not opts.urn:
                raise TypeError("Missing required property 'group_slug'")
            __props__.__dict__["group_slug"] = group_slug
            if user_slug is None and not opts.urn:
                raise TypeError("Missing required property 'user_slug'")
            __props__.__dict__["user_slug"] = user_slug
        super(GroupMember, __self__).__init__(
            'doppler:index/groupMember:GroupMember',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            group_slug: Optional[pulumi.Input[str]] = None,
            user_slug: Optional[pulumi.Input[str]] = None) -> 'GroupMember':
        """
        Get an existing GroupMember resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] group_slug: The slug of the Doppler group
        :param pulumi.Input[str] user_slug: The slug of the Doppler workplace user
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _GroupMemberState.__new__(_GroupMemberState)

        __props__.__dict__["group_slug"] = group_slug
        __props__.__dict__["user_slug"] = user_slug
        return GroupMember(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="groupSlug")
    def group_slug(self) -> pulumi.Output[str]:
        """
        The slug of the Doppler group
        """
        return pulumi.get(self, "group_slug")

    @property
    @pulumi.getter(name="userSlug")
    def user_slug(self) -> pulumi.Output[str]:
        """
        The slug of the Doppler workplace user
        """
        return pulumi.get(self, "user_slug")

