// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

/**
 * Retrieve all secrets in the config.
 */
export function getSecrets(args?: GetSecretsArgs, opts?: pulumi.InvokeOptions): Promise<GetSecretsResult> {
    args = args || {};

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("doppler:index/getSecrets:getSecrets", {
        "config": args.config,
        "project": args.project,
    }, opts);
}

/**
 * A collection of arguments for invoking getSecrets.
 */
export interface GetSecretsArgs {
    /**
     * The name of the Doppler config (required for personal tokens)
     */
    config?: string;
    /**
     * The name of the Doppler project (required for personal tokens)
     */
    project?: string;
}

/**
 * A collection of values returned by getSecrets.
 */
export interface GetSecretsResult {
    /**
     * The name of the Doppler config (required for personal tokens)
     */
    readonly config?: string;
    /**
     * The provider-assigned unique ID for this managed resource.
     */
    readonly id: string;
    /**
     * A mapping of secret names to computed secret values
     */
    readonly map: {[key: string]: string};
    /**
     * The name of the Doppler project (required for personal tokens)
     */
    readonly project?: string;
}
/**
 * Retrieve all secrets in the config.
 */
export function getSecretsOutput(args?: GetSecretsOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetSecretsResult> {
    return pulumi.output(args).apply((a: any) => getSecrets(a, opts))
}

/**
 * A collection of arguments for invoking getSecrets.
 */
export interface GetSecretsOutputArgs {
    /**
     * The name of the Doppler config (required for personal tokens)
     */
    config?: pulumi.Input<string>;
    /**
     * The name of the Doppler project (required for personal tokens)
     */
    project?: pulumi.Input<string>;
}
