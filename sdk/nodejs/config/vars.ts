// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

declare var exports: any;
const __config = new pulumi.Config("doppler");

/**
 * A Doppler token, either a personal or service token
 */
export declare const dopplerToken: string | undefined;
Object.defineProperty(exports, "dopplerToken", {
    get() {
        return __config.get("dopplerToken");
    },
    enumerable: true,
});

/**
 * The Doppler API host (i.e. https://api.doppler.com)
 */
export declare const host: string | undefined;
Object.defineProperty(exports, "host", {
    get() {
        return __config.get("host");
    },
    enumerable: true,
});

/**
 * Whether or not to verify TLS
 */
export declare const verifyTls: boolean | undefined;
Object.defineProperty(exports, "verifyTls", {
    get() {
        return __config.getObject<boolean>("verifyTls");
    },
    enumerable: true,
});

