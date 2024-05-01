// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

/**
 * Retrieve an existing Doppler user.
 *
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as doppler from "@pulumi/doppler";
 *
 * const nic = doppler.getUser({
 *     email: "nic@doppler.com",
 * });
 * ```
 */
export function getUser(args: GetUserArgs, opts?: pulumi.InvokeOptions): Promise<GetUserResult> {

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("doppler:index/getUser:getUser", {
        "email": args.email,
    }, opts);
}

/**
 * A collection of arguments for invoking getUser.
 */
export interface GetUserArgs {
    /**
     * The email address of the Doppler user
     */
    email: string;
}

/**
 * A collection of values returned by getUser.
 */
export interface GetUserResult {
    /**
     * The email address of the Doppler user
     */
    readonly email: string;
    /**
     * The provider-assigned unique ID for this managed resource.
     */
    readonly id: string;
    /**
     * The slug of the Doppler user
     */
    readonly slug: string;
}
/**
 * Retrieve an existing Doppler user.
 *
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as doppler from "@pulumi/doppler";
 *
 * const nic = doppler.getUser({
 *     email: "nic@doppler.com",
 * });
 * ```
 */
export function getUserOutput(args: GetUserOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetUserResult> {
    return pulumi.output(args).apply((a: any) => getUser(a, opts))
}

/**
 * A collection of arguments for invoking getUser.
 */
export interface GetUserOutputArgs {
    /**
     * The email address of the Doppler user
     */
    email: pulumi.Input<string>;
}
