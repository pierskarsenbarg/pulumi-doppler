// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

// Export members:
export { AwsParameterStoreArgs, AwsParameterStoreState } from "./awsParameterStore";
export type AwsParameterStore = import("./awsParameterStore").AwsParameterStore;
export const AwsParameterStore: typeof import("./awsParameterStore").AwsParameterStore = null as any;
utilities.lazyLoad(exports, ["AwsParameterStore"], () => require("./awsParameterStore"));

export { AwsSecretsManagerArgs, AwsSecretsManagerState } from "./awsSecretsManager";
export type AwsSecretsManager = import("./awsSecretsManager").AwsSecretsManager;
export const AwsSecretsManager: typeof import("./awsSecretsManager").AwsSecretsManager = null as any;
utilities.lazyLoad(exports, ["AwsSecretsManager"], () => require("./awsSecretsManager"));

export { TerraformCloudArgs, TerraformCloudState } from "./terraformCloud";
export type TerraformCloud = import("./terraformCloud").TerraformCloud;
export const TerraformCloud: typeof import("./terraformCloud").TerraformCloud = null as any;
utilities.lazyLoad(exports, ["TerraformCloud"], () => require("./terraformCloud"));


const _module = {
    version: utilities.getVersion(),
    construct: (name: string, type: string, urn: string): pulumi.Resource => {
        switch (type) {
            case "doppler:integration/awsParameterStore:AwsParameterStore":
                return new AwsParameterStore(name, <any>undefined, { urn })
            case "doppler:integration/awsSecretsManager:AwsSecretsManager":
                return new AwsSecretsManager(name, <any>undefined, { urn })
            case "doppler:integration/terraformCloud:TerraformCloud":
                return new TerraformCloud(name, <any>undefined, { urn })
            default:
                throw new Error(`unknown resource type ${type}`);
        }
    },
};
pulumi.runtime.registerResourceModule("doppler", "integration/awsParameterStore", _module)
pulumi.runtime.registerResourceModule("doppler", "integration/awsSecretsManager", _module)
pulumi.runtime.registerResourceModule("doppler", "integration/terraformCloud", _module)
