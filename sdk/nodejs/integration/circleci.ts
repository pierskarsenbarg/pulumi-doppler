// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

/**
 * Manage a CircleCI Doppler integration.
 *
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as doppler from "@pulumiverse/doppler";
 *
 * const prod = new doppler.integration.Circleci("prod", {
 *     name: "Production",
 *     apiToken: "my_api_token",
 * });
 * const backendProd = new doppler.secretssync.Circleci("backend_prod", {
 *     integration: prod.id,
 *     project: "backend",
 *     config: "prd",
 *     resourceType: "project",
 *     resourceId: "github/myorg/myproject",
 *     organizationSlug: "myorg",
 *     deleteBehavior: "leave_in_target",
 * });
 * ```
 */
export class Circleci extends pulumi.CustomResource {
    /**
     * Get an existing Circleci resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: CircleciState, opts?: pulumi.CustomResourceOptions): Circleci {
        return new Circleci(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'doppler:integration/circleci:Circleci';

    /**
     * Returns true if the given object is an instance of Circleci.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is Circleci {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === Circleci.__pulumiType;
    }

    /**
     * A CircleCI API token. See https://docs.doppler.com/docs/circleci for details.
     */
    public readonly apiToken!: pulumi.Output<string>;
    /**
     * The name of the integration
     */
    public readonly name!: pulumi.Output<string>;

    /**
     * Create a Circleci resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: CircleciArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: CircleciArgs | CircleciState, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (opts.id) {
            const state = argsOrState as CircleciState | undefined;
            resourceInputs["apiToken"] = state ? state.apiToken : undefined;
            resourceInputs["name"] = state ? state.name : undefined;
        } else {
            const args = argsOrState as CircleciArgs | undefined;
            if ((!args || args.apiToken === undefined) && !opts.urn) {
                throw new Error("Missing required property 'apiToken'");
            }
            if ((!args || args.name === undefined) && !opts.urn) {
                throw new Error("Missing required property 'name'");
            }
            resourceInputs["apiToken"] = args?.apiToken ? pulumi.secret(args.apiToken) : undefined;
            resourceInputs["name"] = args ? args.name : undefined;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        const secretOpts = { additionalSecretOutputs: ["apiToken"] };
        opts = pulumi.mergeOptions(opts, secretOpts);
        super(Circleci.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering Circleci resources.
 */
export interface CircleciState {
    /**
     * A CircleCI API token. See https://docs.doppler.com/docs/circleci for details.
     */
    apiToken?: pulumi.Input<string>;
    /**
     * The name of the integration
     */
    name?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a Circleci resource.
 */
export interface CircleciArgs {
    /**
     * A CircleCI API token. See https://docs.doppler.com/docs/circleci for details.
     */
    apiToken: pulumi.Input<string>;
    /**
     * The name of the integration
     */
    name: pulumi.Input<string>;
}
