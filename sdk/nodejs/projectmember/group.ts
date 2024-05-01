// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

/**
 * Manage a Doppler project group member.
 *
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as doppler from "@pulumiverse/doppler";
 *
 * const backendEngineering = new doppler.projectmember.Group("backend_engineering", {
 *     project: "backend",
 *     groupSlug: engineering.slug,
 *     role: "collaborator",
 *     environments: [
 *         "dev",
 *         "stg",
 *     ],
 * });
 * ```
 */
export class Group extends pulumi.CustomResource {
    /**
     * Get an existing Group resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: GroupState, opts?: pulumi.CustomResourceOptions): Group {
        return new Group(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'doppler:projectMember/group:Group';

    /**
     * Returns true if the given object is an instance of Group.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is Group {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === Group.__pulumiType;
    }

    /**
     * The environments in the project where this access will apply (null or omitted for roles with access to all environments)
     */
    public readonly environments!: pulumi.Output<string[] | undefined>;
    /**
     * The slug of the Doppler group
     */
    public readonly groupSlug!: pulumi.Output<string>;
    /**
     * The name of the Doppler project where the access is applied
     */
    public readonly project!: pulumi.Output<string>;
    /**
     * The project role identifier for the access
     */
    public readonly role!: pulumi.Output<string>;

    /**
     * Create a Group resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: GroupArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: GroupArgs | GroupState, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (opts.id) {
            const state = argsOrState as GroupState | undefined;
            resourceInputs["environments"] = state ? state.environments : undefined;
            resourceInputs["groupSlug"] = state ? state.groupSlug : undefined;
            resourceInputs["project"] = state ? state.project : undefined;
            resourceInputs["role"] = state ? state.role : undefined;
        } else {
            const args = argsOrState as GroupArgs | undefined;
            if ((!args || args.groupSlug === undefined) && !opts.urn) {
                throw new Error("Missing required property 'groupSlug'");
            }
            if ((!args || args.project === undefined) && !opts.urn) {
                throw new Error("Missing required property 'project'");
            }
            if ((!args || args.role === undefined) && !opts.urn) {
                throw new Error("Missing required property 'role'");
            }
            resourceInputs["environments"] = args ? args.environments : undefined;
            resourceInputs["groupSlug"] = args ? args.groupSlug : undefined;
            resourceInputs["project"] = args ? args.project : undefined;
            resourceInputs["role"] = args ? args.role : undefined;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(Group.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering Group resources.
 */
export interface GroupState {
    /**
     * The environments in the project where this access will apply (null or omitted for roles with access to all environments)
     */
    environments?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * The slug of the Doppler group
     */
    groupSlug?: pulumi.Input<string>;
    /**
     * The name of the Doppler project where the access is applied
     */
    project?: pulumi.Input<string>;
    /**
     * The project role identifier for the access
     */
    role?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a Group resource.
 */
export interface GroupArgs {
    /**
     * The environments in the project where this access will apply (null or omitted for roles with access to all environments)
     */
    environments?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * The slug of the Doppler group
     */
    groupSlug: pulumi.Input<string>;
    /**
     * The name of the Doppler project where the access is applied
     */
    project: pulumi.Input<string>;
    /**
     * The project role identifier for the access
     */
    role: pulumi.Input<string>;
}
