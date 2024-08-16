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
    /// Manage a Doppler service account token.
    /// </summary>
    [DopplerResourceType("doppler:index/serviceAccountToken:ServiceAccountToken")]
    public partial class ServiceAccountToken : global::Pulumi.CustomResource
    {
        /// <summary>
        /// The api key used to authenticate the service account
        /// </summary>
        [Output("apiKey")]
        public Output<string> ApiKey { get; private set; } = null!;

        /// <summary>
        /// The datetime that the token was created.
        /// </summary>
        [Output("createdAt")]
        public Output<string> CreatedAt { get; private set; } = null!;

        /// <summary>
        /// The datetime at which the API token should expire. If not provided, the API token will remain valid indefinitely unless manually revoked
        /// </summary>
        [Output("expiresAt")]
        public Output<string?> ExpiresAt { get; private set; } = null!;

        /// <summary>
        /// The display name of the API token
        /// </summary>
        [Output("name")]
        public Output<string> Name { get; private set; } = null!;

        /// <summary>
        /// Slug of the service account
        /// </summary>
        [Output("serviceAccountSlug")]
        public Output<string> ServiceAccountSlug { get; private set; } = null!;

        /// <summary>
        /// Slug of the service account token
        /// </summary>
        [Output("slug")]
        public Output<string> Slug { get; private set; } = null!;


        /// <summary>
        /// Create a ServiceAccountToken resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public ServiceAccountToken(string name, ServiceAccountTokenArgs args, CustomResourceOptions? options = null)
            : base("doppler:index/serviceAccountToken:ServiceAccountToken", name, args ?? new ServiceAccountTokenArgs(), MakeResourceOptions(options, ""))
        {
        }

        private ServiceAccountToken(string name, Input<string> id, ServiceAccountTokenState? state = null, CustomResourceOptions? options = null)
            : base("doppler:index/serviceAccountToken:ServiceAccountToken", name, state, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
                PluginDownloadURL = "github://api.github.com/pulumiverse",
                AdditionalSecretOutputs =
                {
                    "apiKey",
                },
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing ServiceAccountToken resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static ServiceAccountToken Get(string name, Input<string> id, ServiceAccountTokenState? state = null, CustomResourceOptions? options = null)
        {
            return new ServiceAccountToken(name, id, state, options);
        }
    }

    public sealed class ServiceAccountTokenArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The datetime at which the API token should expire. If not provided, the API token will remain valid indefinitely unless manually revoked
        /// </summary>
        [Input("expiresAt")]
        public Input<string>? ExpiresAt { get; set; }

        /// <summary>
        /// The display name of the API token
        /// </summary>
        [Input("name", required: true)]
        public Input<string> Name { get; set; } = null!;

        /// <summary>
        /// Slug of the service account
        /// </summary>
        [Input("serviceAccountSlug", required: true)]
        public Input<string> ServiceAccountSlug { get; set; } = null!;

        public ServiceAccountTokenArgs()
        {
        }
        public static new ServiceAccountTokenArgs Empty => new ServiceAccountTokenArgs();
    }

    public sealed class ServiceAccountTokenState : global::Pulumi.ResourceArgs
    {
        [Input("apiKey")]
        private Input<string>? _apiKey;

        /// <summary>
        /// The api key used to authenticate the service account
        /// </summary>
        public Input<string>? ApiKey
        {
            get => _apiKey;
            set
            {
                var emptySecret = Output.CreateSecret(0);
                _apiKey = Output.Tuple<Input<string>?, int>(value, emptySecret).Apply(t => t.Item1);
            }
        }

        /// <summary>
        /// The datetime that the token was created.
        /// </summary>
        [Input("createdAt")]
        public Input<string>? CreatedAt { get; set; }

        /// <summary>
        /// The datetime at which the API token should expire. If not provided, the API token will remain valid indefinitely unless manually revoked
        /// </summary>
        [Input("expiresAt")]
        public Input<string>? ExpiresAt { get; set; }

        /// <summary>
        /// The display name of the API token
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// Slug of the service account
        /// </summary>
        [Input("serviceAccountSlug")]
        public Input<string>? ServiceAccountSlug { get; set; }

        /// <summary>
        /// Slug of the service account token
        /// </summary>
        [Input("slug")]
        public Input<string>? Slug { get; set; }

        public ServiceAccountTokenState()
        {
        }
        public static new ServiceAccountTokenState Empty => new ServiceAccountTokenState();
    }
}
