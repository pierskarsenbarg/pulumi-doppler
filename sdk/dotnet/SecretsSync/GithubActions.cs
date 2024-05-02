// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;
using Pulumi;

namespace Pulumiverse.Doppler.SecretsSync
{
    /// <summary>
    /// Manage a GitHub Actions Doppler sync.
    /// </summary>
    [DopplerResourceType("doppler:secretsSync/githubActions:GithubActions")]
    public partial class GithubActions : global::Pulumi.CustomResource
    {
        /// <summary>
        /// The name of the Doppler config
        /// </summary>
        [Output("config")]
        public Output<string> Config { get; private set; } = null!;

        /// <summary>
        /// The GitHub repo environment name to sync to (only used when `sync_target` is set to "repo")
        /// </summary>
        [Output("environmentName")]
        public Output<string?> EnvironmentName { get; private set; } = null!;

        /// <summary>
        /// The slug of the integration to use for this sync
        /// </summary>
        [Output("integration")]
        public Output<string> Integration { get; private set; } = null!;

        /// <summary>
        /// Either "all" or "private", based on the which repos you want to have access (only used when `sync_target` is set to "org")
        /// </summary>
        [Output("orgScope")]
        public Output<string?> OrgScope { get; private set; } = null!;

        /// <summary>
        /// The name of the Doppler project
        /// </summary>
        [Output("project")]
        public Output<string> Project { get; private set; } = null!;

        /// <summary>
        /// The GitHub repo name to sync to (only used when `sync_target` is set to "repo")
        /// </summary>
        [Output("repoName")]
        public Output<string?> RepoName { get; private set; } = null!;

        /// <summary>
        /// Either "repo" or "org", based on the resource type to sync to
        /// </summary>
        [Output("syncTarget")]
        public Output<string> SyncTarget { get; private set; } = null!;


        /// <summary>
        /// Create a GithubActions resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public GithubActions(string name, GithubActionsArgs args, CustomResourceOptions? options = null)
            : base("doppler:secretsSync/githubActions:GithubActions", name, args ?? new GithubActionsArgs(), MakeResourceOptions(options, ""))
        {
        }

        private GithubActions(string name, Input<string> id, GithubActionsState? state = null, CustomResourceOptions? options = null)
            : base("doppler:secretsSync/githubActions:GithubActions", name, state, MakeResourceOptions(options, id))
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
        /// Get an existing GithubActions resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static GithubActions Get(string name, Input<string> id, GithubActionsState? state = null, CustomResourceOptions? options = null)
        {
            return new GithubActions(name, id, state, options);
        }
    }

    public sealed class GithubActionsArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The name of the Doppler config
        /// </summary>
        [Input("config", required: true)]
        public Input<string> Config { get; set; } = null!;

        /// <summary>
        /// The GitHub repo environment name to sync to (only used when `sync_target` is set to "repo")
        /// </summary>
        [Input("environmentName")]
        public Input<string>? EnvironmentName { get; set; }

        /// <summary>
        /// The slug of the integration to use for this sync
        /// </summary>
        [Input("integration", required: true)]
        public Input<string> Integration { get; set; } = null!;

        /// <summary>
        /// Either "all" or "private", based on the which repos you want to have access (only used when `sync_target` is set to "org")
        /// </summary>
        [Input("orgScope")]
        public Input<string>? OrgScope { get; set; }

        /// <summary>
        /// The name of the Doppler project
        /// </summary>
        [Input("project", required: true)]
        public Input<string> Project { get; set; } = null!;

        /// <summary>
        /// The GitHub repo name to sync to (only used when `sync_target` is set to "repo")
        /// </summary>
        [Input("repoName")]
        public Input<string>? RepoName { get; set; }

        /// <summary>
        /// Either "repo" or "org", based on the resource type to sync to
        /// </summary>
        [Input("syncTarget", required: true)]
        public Input<string> SyncTarget { get; set; } = null!;

        public GithubActionsArgs()
        {
        }
        public static new GithubActionsArgs Empty => new GithubActionsArgs();
    }

    public sealed class GithubActionsState : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The name of the Doppler config
        /// </summary>
        [Input("config")]
        public Input<string>? Config { get; set; }

        /// <summary>
        /// The GitHub repo environment name to sync to (only used when `sync_target` is set to "repo")
        /// </summary>
        [Input("environmentName")]
        public Input<string>? EnvironmentName { get; set; }

        /// <summary>
        /// The slug of the integration to use for this sync
        /// </summary>
        [Input("integration")]
        public Input<string>? Integration { get; set; }

        /// <summary>
        /// Either "all" or "private", based on the which repos you want to have access (only used when `sync_target` is set to "org")
        /// </summary>
        [Input("orgScope")]
        public Input<string>? OrgScope { get; set; }

        /// <summary>
        /// The name of the Doppler project
        /// </summary>
        [Input("project")]
        public Input<string>? Project { get; set; }

        /// <summary>
        /// The GitHub repo name to sync to (only used when `sync_target` is set to "repo")
        /// </summary>
        [Input("repoName")]
        public Input<string>? RepoName { get; set; }

        /// <summary>
        /// Either "repo" or "org", based on the resource type to sync to
        /// </summary>
        [Input("syncTarget")]
        public Input<string>? SyncTarget { get; set; }

        public GithubActionsState()
        {
        }
        public static new GithubActionsState Empty => new GithubActionsState();
    }
}
