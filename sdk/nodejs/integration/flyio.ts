// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

/**
 * Manage a Fly.io Doppler integration.
 *
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as doppler from "@pulumiverse/doppler";
 *
 * const prod = new doppler.integration.Flyio("prod", {
 *     name: "TF Fly.io",
 *     apiKey: "fo1_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
 * });
 * const backendProd = new doppler.secretssync.Flyio("backend_prod", {
 *     integration: prod.id,
 *     project: "backend",
 *     config: "prd",
 *     appId: "my-app",
 *     restartMachines: true,
 *     deleteBehavior: "leave_in_target",
 * });
 * ```
 */
export class Flyio extends pulumi.CustomResource {
    /**
     * Get an existing Flyio resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: FlyioState, opts?: pulumi.CustomResourceOptions): Flyio {
        return new Flyio(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'doppler:integration/flyio:Flyio';

    /**
     * Returns true if the given object is an instance of Flyio.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is Flyio {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === Flyio.__pulumiType;
    }

    /**
     * A Fly.io API key.
     */
    public readonly apiKey!: pulumi.Output<string>;
    /**
     * The name of the integration
     */
    public readonly name!: pulumi.Output<string>;

    /**
     * Create a Flyio resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: FlyioArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: FlyioArgs | FlyioState, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (opts.id) {
            const state = argsOrState as FlyioState | undefined;
            resourceInputs["apiKey"] = state ? state.apiKey : undefined;
            resourceInputs["name"] = state ? state.name : undefined;
        } else {
            const args = argsOrState as FlyioArgs | undefined;
            if ((!args || args.apiKey === undefined) && !opts.urn) {
                throw new Error("Missing required property 'apiKey'");
            }
            if ((!args || args.name === undefined) && !opts.urn) {
                throw new Error("Missing required property 'name'");
            }
            resourceInputs["apiKey"] = args?.apiKey ? pulumi.secret(args.apiKey) : undefined;
            resourceInputs["name"] = args ? args.name : undefined;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        const secretOpts = { additionalSecretOutputs: ["apiKey"] };
        opts = pulumi.mergeOptions(opts, secretOpts);
        super(Flyio.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering Flyio resources.
 */
export interface FlyioState {
    /**
     * A Fly.io API key.
     */
    apiKey?: pulumi.Input<string>;
    /**
     * The name of the integration
     */
    name?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a Flyio resource.
 */
export interface FlyioArgs {
    /**
     * A Fly.io API key.
     */
    apiKey: pulumi.Input<string>;
    /**
     * The name of the integration
     */
    name: pulumi.Input<string>;
}
