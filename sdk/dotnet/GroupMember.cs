// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;
using Pulumi;

namespace Pulumiverse.Doppler
{
    /// <summary>
    /// Manage a Doppler user/group membership.
    /// 
    /// **Note:** You can also exclusively manage all memberships in a group with a single resource.
    /// See the `doppler.GroupMembers` resource for more information.
    /// 
    /// ## Import
    /// 
    /// import using the group slug from the URL:
    /// 
    /// https://dashboard.doppler.com/workplace/[workplace-slug]/team/groups/[group-slug]
    /// 
    /// and the user slug from the URL:
    /// 
    /// https://dashboard.doppler.com/workplace/[workplace-slug]/team/users/[user-slug]
    /// 
    /// ```sh
    /// $ pulumi import doppler:index/groupMember:GroupMember default &lt;group-slug&gt;.workplace_user.&lt;user-slug&gt;
    /// ```
    /// </summary>
    [DopplerResourceType("doppler:index/groupMember:GroupMember")]
    public partial class GroupMember : global::Pulumi.CustomResource
    {
        /// <summary>
        /// The slug of the Doppler group
        /// </summary>
        [Output("groupSlug")]
        public Output<string> GroupSlug { get; private set; } = null!;

        /// <summary>
        /// The slug of the Doppler workplace user
        /// </summary>
        [Output("userSlug")]
        public Output<string> UserSlug { get; private set; } = null!;


        /// <summary>
        /// Create a GroupMember resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public GroupMember(string name, GroupMemberArgs args, CustomResourceOptions? options = null)
            : base("doppler:index/groupMember:GroupMember", name, args ?? new GroupMemberArgs(), MakeResourceOptions(options, ""))
        {
        }

        private GroupMember(string name, Input<string> id, GroupMemberState? state = null, CustomResourceOptions? options = null)
            : base("doppler:index/groupMember:GroupMember", name, state, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
                PluginDownloadURL = "github://api.github.com/pulumiverse",
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing GroupMember resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static GroupMember Get(string name, Input<string> id, GroupMemberState? state = null, CustomResourceOptions? options = null)
        {
            return new GroupMember(name, id, state, options);
        }
    }

    public sealed class GroupMemberArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The slug of the Doppler group
        /// </summary>
        [Input("groupSlug", required: true)]
        public Input<string> GroupSlug { get; set; } = null!;

        /// <summary>
        /// The slug of the Doppler workplace user
        /// </summary>
        [Input("userSlug", required: true)]
        public Input<string> UserSlug { get; set; } = null!;

        public GroupMemberArgs()
        {
        }
        public static new GroupMemberArgs Empty => new GroupMemberArgs();
    }

    public sealed class GroupMemberState : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The slug of the Doppler group
        /// </summary>
        [Input("groupSlug")]
        public Input<string>? GroupSlug { get; set; }

        /// <summary>
        /// The slug of the Doppler workplace user
        /// </summary>
        [Input("userSlug")]
        public Input<string>? UserSlug { get; set; }

        public GroupMemberState()
        {
        }
        public static new GroupMemberState Empty => new GroupMemberState();
    }
}
