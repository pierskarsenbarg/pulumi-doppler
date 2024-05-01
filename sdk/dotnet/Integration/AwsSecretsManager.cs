// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;
using Pulumi;

namespace Pulumiverse.Doppler.Integration
{
    /// <summary>
    /// Manage an AWS Secrets Manager Doppler integration.
    /// 
    /// ## Example Usage
    /// 
    /// ```csharp
    /// using System.Collections.Generic;
    /// using System.Linq;
    /// using System.Text.Json;
    /// using Pulumi;
    /// using Aws = Pulumi.Aws;
    /// using Doppler = Pulumiverse.Doppler;
    /// 
    /// return await Deployment.RunAsync(() =&gt; 
    /// {
    ///     var dopplerSecretsManager = new Aws.Iam.Role("doppler_secrets_manager", new()
    ///     {
    ///         Name = "doppler_secrets_manager",
    ///         AssumeRolePolicy = JsonSerializer.Serialize(new Dictionary&lt;string, object?&gt;
    ///         {
    ///             ["Version"] = "2012-10-17",
    ///             ["Statement"] = new[]
    ///             {
    ///                 new Dictionary&lt;string, object?&gt;
    ///                 {
    ///                     ["Effect"] = "Allow",
    ///                     ["Action"] = "sts:AssumeRole",
    ///                     ["Principal"] = new Dictionary&lt;string, object?&gt;
    ///                     {
    ///                         ["AWS"] = "arn:aws:iam::299900769157:user/doppler-integration-operator",
    ///                     },
    ///                     ["Condition"] = new Dictionary&lt;string, object?&gt;
    ///                     {
    ///                         ["StringEquals"] = new Dictionary&lt;string, object?&gt;
    ///                         {
    ///                             ["sts:ExternalId"] = "&lt;YOUR_WORKPLACE_SLUG&gt;",
    ///                         },
    ///                     },
    ///                 },
    ///             },
    ///         }),
    ///         InlinePolicies = new[]
    ///         {
    ///             new Aws.Iam.Inputs.RoleInlinePolicyArgs
    ///             {
    ///                 Name = "doppler_secret_manager",
    ///                 Policy = JsonSerializer.Serialize(new Dictionary&lt;string, object?&gt;
    ///                 {
    ///                     ["Version"] = "2012-10-17",
    ///                     ["Statement"] = new[]
    ///                     {
    ///                         new Dictionary&lt;string, object?&gt;
    ///                         {
    ///                             ["Action"] = new[]
    ///                             {
    ///                                 "secretsmanager:GetSecretValue",
    ///                                 "secretsmanager:DescribeSecret",
    ///                                 "secretsmanager:PutSecretValue",
    ///                                 "secretsmanager:CreateSecret",
    ///                                 "secretsmanager:DeleteSecret",
    ///                                 "secretsmanager:TagResource",
    ///                                 "secretsmanager:UpdateSecret",
    ///                             },
    ///                             ["Effect"] = "Allow",
    ///                             ["Resource"] = "*",
    ///                         },
    ///                     },
    ///                 }),
    ///             },
    ///         },
    ///     });
    /// 
    ///     var prod = new Doppler.Integration.AwsSecretsManager("prod", new()
    ///     {
    ///         Name = "Production",
    ///         AssumeRoleArn = dopplerSecretsManager.Arn,
    ///     });
    /// 
    ///     var backendProd = new Doppler.SecretsSync.AwsSecretsManager("backend_prod", new()
    ///     {
    ///         Integration = prod.Id,
    ///         Project = "backend",
    ///         Config = "prd",
    ///         Region = "us-east-1",
    ///         Path = "/backend/",
    ///         Tags = 
    ///         {
    ///             { "myTag", "enabled" },
    ///         },
    ///     });
    /// 
    /// });
    /// ```
    /// </summary>
    [DopplerResourceType("doppler:integration/awsSecretsManager:AwsSecretsManager")]
    public partial class AwsSecretsManager : global::Pulumi.CustomResource
    {
        /// <summary>
        /// The ARN of the AWS role for Doppler to assume
        /// </summary>
        [Output("assumeRoleArn")]
        public Output<string> AssumeRoleArn { get; private set; } = null!;

        /// <summary>
        /// The name of the integration
        /// </summary>
        [Output("name")]
        public Output<string> Name { get; private set; } = null!;


        /// <summary>
        /// Create a AwsSecretsManager resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public AwsSecretsManager(string name, AwsSecretsManagerArgs args, CustomResourceOptions? options = null)
            : base("doppler:integration/awsSecretsManager:AwsSecretsManager", name, args ?? new AwsSecretsManagerArgs(), MakeResourceOptions(options, ""))
        {
        }

        private AwsSecretsManager(string name, Input<string> id, AwsSecretsManagerState? state = null, CustomResourceOptions? options = null)
            : base("doppler:integration/awsSecretsManager:AwsSecretsManager", name, state, MakeResourceOptions(options, id))
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
        /// Get an existing AwsSecretsManager resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static AwsSecretsManager Get(string name, Input<string> id, AwsSecretsManagerState? state = null, CustomResourceOptions? options = null)
        {
            return new AwsSecretsManager(name, id, state, options);
        }
    }

    public sealed class AwsSecretsManagerArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The ARN of the AWS role for Doppler to assume
        /// </summary>
        [Input("assumeRoleArn", required: true)]
        public Input<string> AssumeRoleArn { get; set; } = null!;

        /// <summary>
        /// The name of the integration
        /// </summary>
        [Input("name", required: true)]
        public Input<string> Name { get; set; } = null!;

        public AwsSecretsManagerArgs()
        {
        }
        public static new AwsSecretsManagerArgs Empty => new AwsSecretsManagerArgs();
    }

    public sealed class AwsSecretsManagerState : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The ARN of the AWS role for Doppler to assume
        /// </summary>
        [Input("assumeRoleArn")]
        public Input<string>? AssumeRoleArn { get; set; }

        /// <summary>
        /// The name of the integration
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        public AwsSecretsManagerState()
        {
        }
        public static new AwsSecretsManagerState Empty => new AwsSecretsManagerState();
    }
}
